# auto_abstract
本项目始于大三信息系统设计课程，我与胡彤同学共同完成了该项目初代，我负责完成算法与处理部分，胡彤同学则完成界面部分。虽然第一版的运行情况并不完美，其中也出现了超多bug，不过就项目来说算是一个开始，积累了不少经验，在此很感谢胡彤同学制作的优美的界面。
## v1.0
文本摘要与标题生成算法。
为了解决论文写作过程中的摘要参考与题目参考问题，本项目搭建了训练模型并做出了一个并不完美的模型。

### 使用的算法
  注意力机制的NLP模型
  
  
  sentenceRank算法
  
  
  近义词替换算法

### 主要逻辑
  首先使用sentence算法进行提取关键句，关键句即可成为摘要（抽取式），在一定规模的摘要上，使用NLP模型训练，最终生成题目，文章——摘要——标题

### 主要问题
  1.使用的代码版本过于落后，本项目部分借鉴于较为陈旧的项目，这些项目使用的tensorflow版本甚至已经无法获得。
  
  2.数据源使用的是搜狗实验室的语料数据，但是该数据应该经过有效的处理之后才能使用，本项目对复杂的语料数据并未做过多的处理
  
  3.使用sentenceRank算法得到的摘要有一定的偏差，以至于训练出来的效果不尽人意
  
  4.语料中的标题也是人为生成的，其中不乏标题不实，广告内容等现象。
  
