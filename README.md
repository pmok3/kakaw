# Kakaw! Machine Learning for Sports Betting
Kakaw! was started in January 2020 as an effort to predict NCAA Basketball winning outcomes using real time game data. Game data from previous years was collected and fed into an LSTM machine learning model to predict the outcome of a game in real time. The project was paused during the coronavirus pandemic, where all NCAA games would eventually be halted.

In May 2023, the idea of Kakaw was resurrected from trends in the NBA that I believe have statistical significance and may play a key role in correctly profiting from game outcomes.

#### Disclaimer: Kakaw! is merely a simple predictive model and claims no level of statistical certainty. Do not blindly follow its picks, and watch the games yourself live to see if your own judgment aligns with Kakaw!'s picks before making any financial decisions. 

## The idea
For years, basketball had been considered the least random of sports; that is to say, if your team has the more skilled players, you have a significantly higher chance of winning. Since the 2015-16 season, however, the steady rise of the 3pt shot has posed challenge to that claim. As teams reformulated their offensive and defensive schemes around data analytics, 3 pointers and dunks became favoured over the iso-style midrange game. Players who stayed in the league were forced to adapt their own skillsets accordingly; most players now have some sort of a serviceable long range option. Gone are the days of FT tanking centers like Shaq, and in are the new stretch 5's that can space the floor. The variance in scoring patterns due to the increased usage of the 3pt shot has made the NBA standings more uniformly distributed - especially in the 2022-23 season, where seeds 5-14 of the Western Conference were separated by 3.5 games for the majority of the season - and because of this, an opportunity has arisen that can be explored in the context of sports betting.

Kakaw! aims to capitalize on scoring patterns and betting odds data to make real time predictions on who the game's winner will be. Kakaw!'s goals are to maximize profit made from moneyline betting, and will not engage in over/under predictions, nor will it attempt to predict individual player or aggregate team statistics.

## A note on Machine Learning
Generative artificial intelligence and other large language based machine learning models are the talk of the town these days. Kakaw! will not use machine learning in any significant capacity for its decision making. Since the intent of machine learning is to recognize trends within an innumerable quantity of variables to approximate basketball judgment, I see no need to employ these models. The game of basketball is fluid and rapidly changing, and no amount of datasets can account for new rule implementations - the Coach's Challenge comes to mind - that have the potential to drastically alter game outcomes in previous eras if played in today's environment.

## Overview of components
The section below briefly describes the main components of Kakaw!. As the project progresses, I will include more technical details about each component in its own dedicated section.

### Sourcing historical game data (To be completed)
A web scraper will be used to collect play by play data from ESPN's historical archive. Once completed, this will be integrated into github actions and run at midnight every day to collect new game data during the NBA season.

### Sourcing historical odds data (To be completed)
A web scraper will be used to collect historical moneyline odds from the OddsPortal archive. These odds are recorded before tip off and represent an average of the lines offered by major betting sites.

### Backtesting engine for bet criterion development (To be completed)
An engine will be created that applies user-specified criterion to historical game data and reports statistical information to the user.

### Sourcing live betting odds data (To be completed)
A web scraper will be used to collect live betting odds data from bodog.eu.

### Semi-supervised machine learning model (To be completed)
Using a small sample of live odds data collected during the 2023-2024 NBA season, historical game data will be annotated with projected odds. This will provide greater confluence with backtesting new strategies.

### Real-Time Game Screener (To be completed)
Once the above components are completed and a profitable betting strategy is established, a game screener will be created that takes into consideration present and past data from current games and betting data. The screener will have API endpoints that connect with lightweight programs on desktop and mobile platforms. 

### Notification system (To be completed)
A notification system will be created that leverages the real-time game screener to alert users of potential betting opportunities. The design of this system will focus on servicing a large number of users and achieving low latency. For desktop users, this will take the form of a web extension. For mobile users, this will take the form of a mobile app. 

### Infrastructure (To be implemented)
Github will serve as the main code repository. Github actions will be utilized for unit testing and historical data collection. The real-time program will initially be run locally on a spare laptop. If the project is proven to be worthwhile, I will look into hosting it on AWS.
