WorldCup-Betting-in-Python

==============================================================================================================
Description

Use social media data to predict the poll in betting. Hence, we can make use of this information to win money!


==============================================================================================================
Main idea

1. How we take advantage if we pocess extra information?
    Think of a gambling:

    Guess           WIN     LOSE    DRAW
    Probability     0.33    0.33    0.33
    Rate            3       3       3

    If you know "WIN" can never happen in this game, then you can evenly bet on "LOSE" and "DRAW". Thus NO Matter it is "LOSE" and "DRAW", you always get 50%*3 = 150% of your money back. So you earn 50% advantage in this game.

2. How can we find the most impossible situation?
    ASSUMPTION: you can never win gambling company! because they have the best actuary in the world! so gambling company rarely LOSE big money.

    IDEA:
    if we know the world bet 30% on WIN, 60% on LOSE, 10% on DRAW, then with the given Rate setting, we can easily calculate which results cost gambling company most. In other word, most impossible result.

3. How can we find the distribution betting on 3 GUESS?
    sentimental analysis on tweets public stream.

    We can extract all the sentimate words like "suck", "A beat B", "die", "super" and the positive and negative signal words like "NOT", "hardly", "never", "alwasy". Based on this, we can evaluate the tweets 1-5 scores on believing team A beats team B. There's a package NLTK(nature language toolkits) in PYTHON can help us analyze tweets.

    ASSUMPTION:
        The more people mentioned gambling and soccer, the more possible he bet large money in gambling.

    So we can roughly estimate the distribution of the money


==============================================================================================================
Functionality Unit Test:

Project file system

    |--- Root
        |--- raw_tweet (universal public tweets stream stored here)
            |--- year_month_day_hour_minute_second.txt
            ...
        |--- processed_data (extracted tweets stored here)
            |--- 001.txt
            |--- 002.txt
            ...
            
    tweeter_public_stream.py (real-time non-stop data streaming, save data into folder "raw_tweet")
    public_stream_processer.py (real-time process "raw_tweet")
    public_poll_analysis.py (analysis the processed_data, predict the poll in "win", "draw" and "lose")
    optimum_betting.py (anlysis the betting-line data, generate the optimum betting strategy)
    
==============================================================================================================
AWS pig server Unit Test:

Project file system & Mapreduce algorithm schema

    |--- Master
        |--- Node1
        |--- Node2
        ...
        |--- Node10

Map:

    Game ID : tweets.json = {'user ID': ...,
                             'text': ...,
                             'location': ...,
                             ...}

Reduce:

    user ID : sentimate value
    user ID : money weight value
