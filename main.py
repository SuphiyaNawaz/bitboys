from flask import Flask, render_template,request
from selenium import webdriver

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')




# prices=driver.find_elements_by_css_selector(".priceValue span")
# for price in prices:
#     print(price.text)



app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/Current_Details")
def Current_Details():
    return render_template('newIndex.html')

@app.route("/receive_data",methods=["post"])
def receive_data():
    chrome_driver_path = "C:\Development\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    coin=request.form["coin"]
    coin_small=coin.lower()
    if coin_small=="bitcoin" or coin_small=="bit" or coin_small=="btc" :
        symbol="BTC"
        img="static/bitcoin.jpg"
        driver.get("https://coinmarketcap.com/currencies/bitcoin/")
        price = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small=="ethereum" or coin_small=="ethereum coin" or coin_small=="ETH":
        driver.get("https://coinmarketcap.com/currencies/ethereum/")
        price = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        symbol="ETH"
        img="static/Ethereum.jpg"
        final_price = price.text
        driver.close()
    elif coin_small=="solana" or coin_small=="solana coin" or coin_small=="sol":
        symbol="SOL"
        img="static/solana.png"
        driver.get("https://coinmarketcap.com/currencies/solana/")
        price = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small=="axie infinity" or coin_small=="axieinfinity" or coin_small=="axs":
        symbol="AXS"
        img="static/Axie.jpg"
        driver.get("https://coinmarketcap.com/currencies/axie-infinity/")
        price = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small=="avalanche" or coin_small=="avalanche coin" or coin_small=="avax":
        symbol="AVAX"
        img="static/Avalanche.png"
        driver.get("https://coinmarketcap.com/currencies/avalanche/")
        price = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "kadena" or coin_small == "kadene" or coin_small == "kda":
        symbol = "KDA"
        img = "static/Kadena.jpg"
        driver.get("https://coinmarketcap.com/currencies/kadena/")
        price = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "crypto.com" or coin_small == "cryptodotcom" or coin_small == "cro":
        symbol = "CRO"
        img = "static/CryptoDotCom.jpg"
        driver.get("https://coinmarketcap.com/currencies/crypto-com-coin/")
        price = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "verasity" or coin_small == "verasity coin" or coin_small == "vra":
        symbol = "VRA"
        img = "static/Verasity.jpg"
        driver.get("https://coinmarketcap.com/currencies/verasity/")
        price = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "polkadot" or coin_small == "polkadot coin" or coin_small == "dot" or coin_small=="digital insurance token":
        symbol = "DOT"
        img = "static/Polkadot.jpg"
        driver.get("https://coinmarketcap.com/currencies/digital-insurance-token/")
        price = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "kucoin" or coin_small == "ku" or coin_small == "kcs":
        symbol = "KCS"
        img = "static/Kucoin.png"
        driver.get("https://coinmarketcap.com/currencies/kucoin-token/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "phantasma" or coin_small == "phantasma coin" or coin_small == "soul":
        symbol = "SOUL"
        img = "static/Phantasma.jpg"
        driver.get("https://coinmarketcap.com/currencies/phantasma/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "binance" or coin_small == "binance coin" or coin_small == "bnb":
        symbol = "BNB"
        img = "static/Binance.jpg"
        driver.get("https://coinmarketcap.com/currencies/binance-coin/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "live peer" or coin_small == "live peer" or coin_small == "lpt":
        symbol = "LPT"
        img = "static/LivePeer.jpg"
        driver.get("https://coinmarketcap.com/currencies/livepeer/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "enjin coin" or coin_small == "enjin" or coin_small == "enj":
        symbol = "ENJ"
        img = "static/Enjin.jpg"
        driver.get("https://coinmarketcap.com/currencies/enjin-coin/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "fantom" or coin_small == "fantom coin" or coin_small == "ftm":
        symbol = "FTM"
        img = "static/Fantom.jpg"
        driver.get("https://coinmarketcap.com/currencies/fantom/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "coti" or coin_small == "coti coin" or coin_small == "coti":
        symbol = "COTI"
        img = "static/Coti.jpg"
        driver.get("https://coinmarketcap.com/currencies/coti/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "sandbox" or coin_small == "sand box" or coin_small == "sand":
        symbol = "SAND"
        img = "static/SandBox.png"
        driver.get("https://coinmarketcap.com/currencies/sandbox/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "polkabridge" or coin_small == "polka bridge" or coin_small == "pbr":
        symbol = "PBR"
        img = "static/PolkaBridge.png"
        driver.get("https://coinmarketcap.com/currencies/polkabridge/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "helium" or coin_small == "helium coin" or coin_small == "hnt":
        symbol = "HNT"
        img = "static/Helium.jpg"
        driver.get("https://coinmarketcap.com/currencies/helium/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "polkastarter" or coin_small == "polka starter" or coin_small == "pols":
        symbol = "POLS"
        img = "static/Polkastarter.png"
        driver.get("https://coinmarketcap.com/currencies/polkastarter/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "kusama" or coin_small == "kusama coin" or coin_small == "ksm":
        symbol = "KSM"
        img = "static/Kusama.png"
        driver.get("https://coinmarketcap.com/currencies/kusama/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "lite coin" or coin_small == "lite" or coin_small == "ltc" or coin_small=="litecoin":
        symbol = "LTC"
        img = "static/LiteCoin.jpg"
        driver.get("https://coinmarketcap.com/currencies/litecoin/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "polkamarkets" or coin_small == "polka markets" or coin_small == "polk":
        symbol = "POLK"
        img = "static/PolkaMarkets.jpg"
        driver.get("https://coinmarketcap.com/currencies/polkamarkets/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "revv" or coin_small == "revv motor sport" or coin_small == "revvmotorsport":
        symbol = "REVV"
        img = "static/REVVMotorSport.png"
        driver.get("https://coinmarketcap.com/currencies/revv/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "1inch network" or coin_small == "1inch" or coin_small == "1inchnetwork":
        symbol = "1INCH"
        img = "static/1inch.png"
        driver.get("https://coinmarketcap.com/currencies/1inch/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "decentraland" or coin_small == "decentraland coin" or coin_small == "mana":
        symbol = "MANA"
        img = "static/decentraland.jpg"
        driver.get("https://coinmarketcap.com/currencies/decentraland/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "illuvium" or coin_small == "illuvium coin" or coin_small == "ilv":
        symbol = "ILV"
        img = "static/Illuvium.jpg"
        driver.get("https://coinmarketcap.com/currencies/illuvium/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "zcash" or coin_small == "zcash coin" or coin_small == "zec":
        symbol = "ZEC"
        img = "static/zcash.png"
        driver.get("https://coinmarketcap.com/currencies/zcash/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "gnosis" or coin_small == "gnosis coin" or coin_small == "gno" or coin_small=="gnosis gno":
        symbol = "GNO"
        img = "static/GNO.png"
        driver.get("https://coinmarketcap.com/currencies/gnosis-gno/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "wilder world" or coin_small == "wilderworld" or coin_small == "wild":
        symbol = "WILD"
        img = "static/WilderWorld.png"
        driver.get("https://coinmarketcap.com/currencies/wilder-world/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "loopring" or coin_small == "loopring coin" or coin_small == "lrc" :
        symbol = "LRC"
        img = "static/Loopring.png"
        driver.get("https://coinmarketcap.com/currencies/loopring/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "storj" or coin_small == "storj coin" or coin_small == "stor":
        symbol = "STOR"
        img = "static/Storj.png"
        driver.get("https://coinmarketcap.com/currencies/storj/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "hive" or coin_small == "hive coin":
        symbol = "HIVE"
        img = "static/Hive.png"
        driver.get("https://coinmarketcap.com/currencies/hive-blockchain/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "quant" or coin_small == "quant coin" or coin_small == "qnt":
        symbol = "QNT"
        img = "static/Quant.jpg"
        driver.get("https://coinmarketcap.com/currencies/quant/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "mint club" or coin_small == "mintclub" or coin_small == "mint":
        symbol = "MINT"
        img = "static/Mint CLub.png"
        driver.get("https://coinmarketcap.com/currencies/mnt-club/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "nervos network" or coin_small == "ckb" or coin_small == "nervosnetwork":
        symbol = "CKB"
        img = "static/Nervos Network.jpg"
        driver.get("https://coinmarketcap.com/currencies//")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "serum" or coin_small == "serum coin" or coin_small == "srm":
        symbol = "SRM"
        img = "static/Serum.png"
        driver.get("https://coinmarketcap.com/currencies/serum/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "tezos" or coin_small == "tezos coin" or coin_small == "xtz":
        symbol = "XTZ"
        img = "static/Tezos.png"
        driver.get("https://coinmarketcap.com/currencies/tezos/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "thorchain" or coin_small == "thorchain coin" or coin_small == "rune":
        symbol = "RUNE"
        img = "static/Throchain.jpg"
        driver.get("https://coinmarketcap.com/currencies/thorchain/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "algorand" or coin_small == "algo" or coin_small == "algorand coin":
        symbol = "ALGO"
        img = "static/Algorand.png"
        driver.get("https://coinmarketcap.com/currencies/algorand/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "polkacity" or coin_small == "polka city" or coin_small == "polc":
        symbol = "POLC"
        img = "static/Polka City.png"
        driver.get("https://coinmarketcap.com/currencies/polkacity/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "oasis" or coin_small == "oasisnetwork" or coin_small == "oasis network" or coin_small=="rose":
        symbol = "ROSE"
        img = "static/Rose.png"
        driver.get("https://coinmarketcap.com/currencies/oasis-network/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "star atlas" or coin_small == "staratlas" or coin_small == "atlas":
        symbol = "ATLAS"
        img = "static/Star Atlas.png"
        driver.get("https://coinmarketcap.com/currencies/star-atlas/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "gala" or coin_small == "gala coin" :
        symbol = "GALA"
        img = "static/Gala.png"
        driver.get("https://coinmarketcap.com/currencies/gala/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "ren" or coin_small == "ren coin" :
        symbol = "REN"
        img = "static/Ren.png"
        driver.get("https://coinmarketcap.com/currencies/ren/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "revomon" or coin_small == "revo" or coin_small == "revomon coin":
        symbol = "REVO"
        img = "static/Revomom.jpg"
        driver.get("https://coinmarketcap.com/currencies/revomon/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "vulgan forced pyr" or coin_small == "pyr" or coin_small == "vulganforced" or coin_small=="vulganforced pyr":
        symbol = "PYR"
        img = "static/VulcanForgedPYR.jpg"
        driver.get("https://coinmarketcap.com/currencies/vulcan-forged-pyr/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "vechain" or coin_small == "vet" or coin_small == "ve chain":
        symbol = "VET"
        img = "static/VeChain.png"
        driver.get("https://coinmarketcap.com/currencies/vechain/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "saitamainu" or coin_small == "saitama inu" or coin_small == "saitama":
        symbol = "SAITAMA"
        img = "static/SaitamaInu.jpg"
        driver.get("https://coinmarketcap.com/currencies/saitama-inu/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "piccoloinu" or coin_small == "pinu" or coin_small == "piccolo inu":
        symbol = "PINU"
        img = "static/Piccolo Inu.jpg"
        driver.get("https://coinmarketcap.com/currencies/piccolo-inu/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    elif coin_small == "floki" or coin_small == "floki inu" or coin_small == "flokiinu":
        symbol = "FLOKI"
        img = "static/FlokiInu.png"
        driver.get("https://coinmarketcap.com/currencies/floki-inu/")
        price = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span')
        final_price = price.text
        driver.close()
    else:
        final_price="Guess there is no such coin! Instead try with symbol of coin"
        symbol="##"
        img="static/Error.jpg"
    return render_template('finalIndex.html', coin= coin, price=final_price,symbol=symbol,img_src=img)


if __name__ == '__main__':
    app.run(debug=True)