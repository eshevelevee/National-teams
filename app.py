from player import Player

player_name = str(input("Введите полное имя футболиста: "))
player_dob = str(input("Введите дату рождения в формате 19991231: ")).rstrip()
player_transfermarkt_link = str(input("Введите ссылку на профиль игрока в Transfermarkt: ")).rstrip()
player_instat_link = str(input("Введите ссылку на профиль игрока в Instat: ")).rstrip()
player1 = Player(player_name, player_dob)

if player_transfermarkt_link:
    player1.add_transfermarkt_link(player_transfermarkt_link)

if player_instat_link:
    player1.add_instat_link(player_instat_link)

# попробовать сначала спрашивать ссылку на транфермаркт и если есть, то парсить имя и дату рождения оттуда



print(player1.fullname)
print(player1.dob)
print(player1.transfermarkt_link)
print(player1.instat_link)
print(player1.instat_id)



