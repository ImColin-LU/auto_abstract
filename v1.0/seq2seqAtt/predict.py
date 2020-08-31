#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
Predict Method for Testing
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
import codecs

import numpy as np
from six.moves import xrange
import tensorflow as tf

from seq2seqAttSum import eval, data_utils
from seq2seqAttSum.headline import LargeConfig

config = LargeConfig()          # new Large Config, 
FLAGS = tf.app.flags.FLAGS      # Reuse the tf.app.flags from headline module

from seq2seqAttSum.headline import create_model
from seq2seqAttSum.headline import buckets
buckets = buckets

def decode():
  '''
  Manually input sentence interactively and the headline will be printed out
  '''
  with tf.Session() as sess:
    # Create model and load parameters.
    model = create_model(sess, True)
    model.batch_size = FLAGS.batch_size   #repeat single sentence 10 times as one batch  # We decode one sentence at a time.
    
    # Load vocabularies.
    vocab_path = os.path.join(FLAGS.data_dir,"vocab")
    vocab, rev_vocab = data_utils.initialize_vocabulary(vocab_path)
    
    # Decode from standard input interactively
    sys.stdout.write("> ")
    sys.stdout.flush()
    sentence = sys.stdin.readline()

    while sentence:
      if (len(sentence.strip('\n')) == 0):
        sys.stdout.flush()
        sentence = sys.stdin.readline()
      # Get token-ids for the input sentence.
      sen=tf.compat.as_bytes(sentence)
      sen=sen.decode('utf-8')
      token_ids = data_utils.sentence_to_token_ids(sen, vocab, normalize_digits=False)
      #print (token_ids) # print token ids
      # Which bucket does it belong to?
      bucket_id = min([b for b in xrange(len(buckets)) if buckets[b][0] > len(token_ids)])
      # Get a 1-element batch to feed the sentence to the model.
      print ("current bucket id" + str(bucket_id))
      encoder_inputs, decoder_inputs, target_weights = model.get_batch(
          {bucket_id: [(token_ids, [])]}, bucket_id)
      
      # Get output logits for the sentence.
      _, _, output_logits_batch = model.step(sess, encoder_inputs, decoder_inputs, target_weights, bucket_id, True)
      # This is a greedy decoder - outputs are just argmaxes of output_logits.     
      output_logits = []
      for item in output_logits_batch:
        output_logits.append(item[0])
      
     # print (output_logits)
     # print (len(output_logits))
     # print (output_logits[0])


      outputs=[]
      for logit in output_logits:
        m=int(np.argmax(logit))
        if m ==3:
          logit[3]=logit[np.argmin(logit)]
          m=int(np.argmax(logit))
        outputs.append(m)

      #outputs = [int(np.argmax(logit)) for logit in output_logits]
      #print(outputs)
      #print(output_logits)
      # If there is an EOS symbol in outputs, cut them at that point.
      if data_utils.EOS_ID in outputs:
        outputs = outputs[:outputs.index(data_utils.EOS_ID)]
      print(" ".join([tf.compat.as_str(rev_vocab[output]) for output in outputs]))
      print("> ", end="")
      sys.stdout.flush()
      sentence = sys.stdin.readline()



def main(_):
  decode()
  


if __name__ == "__main__":
  tf.app.run()
