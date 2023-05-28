# Kakaw! Machine Learning for Sports Betting
Kakaw was started in January 2020 as an effort to predict NCAA Basketball winning outcomes using real time game data. Game data from previous years were collected and fed into an LSTM machine learning model to predict the outcome of a game in real time. The project was paused during the coronavirus pandemic, where all NCAA games would eventually be halted.

In May 2023, the idea of Kakaw was resurrected from trends in the NBA that I believe have statistical significance and may play a key role in correctly profiting from game outcomes.

## The idea
The steady rise of the 3pt shot in the NBA since the 2015-16 season has led to a new archetype of player: the 3 & D guard. It is not uncommmon for teams in today's NBA to sign top shooting talent to albatross contracts; in fact, it is considered essential to have one or more of these players on a roster to stay competitive. The natural variance of the 3pt shot exacerbates the natural phenomenon of scoring runs from either team. Anecdotally, the rise of "trap game" mentions on social media (Trap games refer to the phenomenon of a team playing without major contributors, yet still winning the game) seems to correlate with these scoring trends. 

In the 2022-2023 regular season, the Western Conference had an unparalleled level of parity, with teams from seeds 5-14 being separated by a handful of games for the first 60 games. The rise of the 3 & D guard has helped to nullify the effect of superstar teams in the regular season; the new NBPA deal that discourages superteams will only help create more parity in the league.

The idea that Kakaw! plans to capitalize on therefore, are these scoring runs. Sports betting sites such as DraftKings and FanDuel act as market makers and are thus forced to stay directionally neutral to maintain a low risk profile. This means that their source of income is commissions - they call this the vig for some reason - and odds are thus determined by the consensus of human bettors. This presents an opportunity to see if the Kakaw! model can be viable.

## The plan
The below describes the main components of Kakaw!. As the project progresses, I will include more technical details about each of the components.

### Sourcing historical game data (To be completed)
A web scraper will be used to collect play by play data from ESPN's historical archive. Once completed, this will be integrated into github actions and run at midnight every day to collect new game data during the NBA season.

### Backtesting engine for bet criterion development (To be completed)
An engine will be created that applies user-specified criterion to historical game data and reports statistical information to the user.

### Sourcing live betting odds data (To be completed)
A web scraper will be used to collect live betting odds data from bodog.eu. The target for completion is September 2023.

### Semi-supervised machine learning model (To be completed)
Using a small sample of live odds data collected during the 2023-2024 NBA season, historical game data will be annotated with projected odds. This will provide greater confluence with backtesting new strategies.

### Notification system (To be completed)
Once the above components are completed and a profitable betting strategy is established, a notification system will be created that leverages live real time game and betting data to notify users of a potential betting opportunity. The design of this system will focus on servicing a large number of users and achieving low latency. For desktop users, this will take the form of a web extension. For mobile users, this will take the form of a mobile app. 

### Infrastructure (To be implemented)
Github will serve as the main code repository. Github actions will be utilized for unit testing and historical data collection. The real-time program will initially be run locally on a spare laptop. If the project is proven to be profitable, I will look into hosting it on AWS.
