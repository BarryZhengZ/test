import CoinClass as c


def show_coin_status(coin_obj):
   print(f"This side is up: {coin_obj.get_sideup()}")


def flip(coin_obj):
   coin_obj.toss()


my_coin = c.Coin()


show_coin_status(my_coin)
flip(my_coin)
show_coin_status(my_coin)

