

leagues_url_dict = {'CL.csv': "https://www.betexplorer.com/soccer/europe/champions-league-2011-2012/results/?stage"
                              "=lQm4VbMn",
                    'EL.csv': "https://www.betexplorer.com/soccer/england/premier-league/results/",
                    'England.csv': "https://www.betexplorer.com/soccer/england/premier-league/results/",
                    'England2.csv': "https://www.betexplorer.com/soccer/england/championship/results/",
                    'England2_19-20.csv': "https://www.betexplorer.com/soccer/england/championship-2019-2020/results/",
                    'England2_21-22.csv': "https://www.betexplorer.com/soccer/england/championship-2021-2022/results/",
                    'England2_20-21.csv': "https://www.betexplorer.com/soccer/england/championship-2020-2021/results/",
                    'England3.csv': "https://www.betexplorer.com/soccer/england/league-one/results/",
                    'England4.csv': "https://www.betexplorer.com/soccer/england/league-two/results/",
                    'England16-17.csv': "https://www.betexplorer.com/soccer/england/premier-league-2016-2017/results/",
                    'England17-18.csv': "https://www.betexplorer.com/soccer/england/premier-league-2017-2018/results/",
                    'England20-21.csv': "https://www.betexplorer.com/soccer/england/premier-league-2020-2021/results/",
                    'England21-22.csv': "https://www.betexplorer.com/soccer/england/premier-league-2021-2022/results/",
                    'England19-20.csv': "https://www.betexplorer.com/soccer/england/premier-league-2019-2020/results/",
                    'England18-19.csv': "https://www.betexplorer.com/soccer/england/premier-league-2018-2019/results/",
                    'Argentina.csv': "https://www.betexplorer.com/soccer/argentina/liga-profesional/results/",
                    'Australia.csv': "https://www.betexplorer.com/soccer/australia/a-league/results/",
                    'Austria.csv': "https://www.betexplorer.com/soccer/austria/bundesliga/results/",
                    'Austria20-21.csv': "https://www.betexplorer.com/soccer/austria/tipico-bundesliga-2020-2021/results"
                                        "/?stage=r1wcGlvr",
                    'Belgium.csv': "https://www.betexplorer.com/soccer/belgium/jupiler-pro-league/results/",
                    'Brazil.csv': "https://www.betexplorer.com/soccer/brazil/serie-a/results/",
                    'Chile.csv': "https://www.betexplorer.com/soccer/chile/primera-division/results/",
                    'France.csv': "https://www.betexplorer.com/soccer/france/ligue-1/results/",
                    'France2.csv': "https://www.betexplorer.com/soccer/france/ligue-2/results/",
                    'France18-19.csv': "https://www.betexplorer.com/soccer/france/ligue-1-2018-2019/results/",
                    'France19-20.csv': "https://www.betexplorer.com/soccer/france/ligue-1-2019-2020/results/",
                    'France20-21.csv': "https://www.betexplorer.com/soccer/france/ligue-1-2020-2021/results/",
                    'France21-22.csv': "https://www.betexplorer.com/soccer/france/ligue-1-2021-2022/results/",
                    'Germany.csv': "https://www.betexplorer.com/soccer/germany/bundesliga/results/",
                    'Germany2.csv': "https://www.betexplorer.com/soccer/germany/2-bundesliga/results/",
                    'Germany18-19.csv': "https://www.betexplorer.com/soccer/germany/bundesliga-2018-2019/results/",
                    'Germany19-20.csv': "https://www.betexplorer.com/soccer/germany/bundesliga-2019-2020/results/",
                    'Germany20-21.csv': "https://www.betexplorer.com/soccer/germany/bundesliga-2020-2021/results/",
                    'Germany21-22.csv': "https://www.betexplorer.com/soccer/germany/bundesliga-2021-2022/results/",
                    'Greece.csv': "https://www.betexplorer.com/soccer/greece/super-league/results/",
                    'Italy.csv': "https://www.betexplorer.com/soccer/italy/serie-a/results/",
                    'Italy2.csv': "https://www.betexplorer.com/soccer/italy/serie-b/results/",
                    'Italy18-19.csv': "https://www.betexplorer.com/soccer/italy/serie-a-2018-2019/results/",
                    'Italy19-20.csv': "https://www.betexplorer.com/soccer/italy/serie-a-2019-2020/results/",
                    'Italy20-21.csv': "https://www.betexplorer.com/soccer/italy/serie-a-2020-2021/results/",
                    'Italy21-22.csv': "https://www.betexplorer.com/soccer/italy/serie-a-2021-2022/results/",
                    'Japan.csv': "https://www.betexplorer.com/soccer/japan/j1-league/results/",
                    'Netherlands.csv': "https://www.betexplorer.com/soccer/netherlands/eredivisie/results/",
                    'Poland.csv': "https://www.betexplorer.com/soccer/poland/ekstraklasa/results/",
                    'Portugal.csv': "https://www.betexplorer.com/soccer/portugal/liga-portugal-2021-2022/results/",
                    'Scotland.csv': "https://www.betexplorer.com/soccer/scotland/premiership/results/",
                    'Spain.csv': "https://www.betexplorer.com/soccer/spain/laliga/results/",
                    'Spain2.csv': "https://www.betexplorer.com/soccer/spain/laliga2-2021-2022/results/",
                    'Spain18-19.csv': "https://www.betexplorer.com/soccer/spain/laliga-2018-2019/results/",
                    'Spain19-20.csv': "https://www.betexplorer.com/soccer/spain/laliga-2019-2020/results/",
                    'Spain20-21.csv': "https://www.betexplorer.com/soccer/spain/laliga-2020-2021/results/",
                    'Spain21-22.csv': "https://www.betexplorer.com/soccer/spain/laliga-2021-2022/results/",
                    'Sweden.csv': "https://www.betexplorer.com/soccer/sweden/allsvenskan/results/",
                    'Switzerland.csv': "https://www.betexplorer.com/soccer/switzerland/super-league/results/",
                    'Turkey.csv': "https://www.betexplorer.com/soccer/turkey/super-lig/results/",
                    'Turkey20-21.csv': "https://www.betexplorer.com/soccer/turkey/super-lig-2020-2021/results/",
                    'USA.csv': "https://www.betexplorer.com/soccer/usa/mls/results/",
                    'England145.csv': "https://www.betexplorer.com/soccer/usa/mls/results/"}
