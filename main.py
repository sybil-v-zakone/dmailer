from loguru import logger

from modules import run_mailer

start_message = r"""

                                  ^Y                  
                                 ~&@7                
                      75~:.     !@&~&:       , .      
                      .&&PYY7^.7@@# J#   .^7JPB^      
                       ^@&Y:^?Y&@@P  GBB&@@GP&~       
                        7@@&?  :&@J  G@@&Y.~#^        
                     .:~?&#&@&? !@! B@G~  !&:         
                :75PPY?!^. .:?GG~P!5P~^!YG@@GJ~.      
                .~YG#&&##B#BGPJ?J??J?J5GBBBB##&#B5!.  
                    .^?P&@BJ!^^5G~G^5GJ^. .:!?Y5P57:\  
                       .#?  ^P@#.:@J !&@@#&J~^.       
                      :#7.J&@@#. !@@~  !&@@5          
                     ^&GP@@&BG#. J@@@5?~:?&@7         
                    :BGJ7^..  GG P@@J.:!JY5&@:        
                    .         .&7B@?      .~YJ        
                              ^&@7                   
                                ?!                  
                                                                       
               __    _ __                        __                  
   _______  __/ /_  (_) /  _   __   ____  ____ _/ /______  ____  ___ 
  / ___/ / / / __ \/ / /  | | / /  /_  / / __ `/ //_/ __ \/ __ \/ _ \
 (__  ) /_/ / /_/ / / /   | |/ /    / /_/ /_/ / ,< / /_/ / / / /  __/   
/____/\__, /_.___/_/_/    |___/    /___/\__,_/_/|_|\____/_/ /_/\___/ 
     /____/      
                                              
"""


def main():
    logger.debug(start_message)
    input("To start press enter...")

    run_mailer()


if __name__ == "__main__":
    main()
