import time
import os
import subprocess
from PIL import Image
from alive_progress import alive_bar

ID = '7e0227c5'
DEVICE = '-s ' + ID
WAIT_TIME = 4
INSTALL_WAIT_TIME = 45
SCREENSHOT_FILENAME = f'screen-{ID}.png'
BLUE = (168, 199, 250, 255)
GREEN = (0, 97, 110, 255)
GREY = (176, 190, 197, 255)
GREEN_PIXELS = [(300, 750), (360, 875), (710, 590), (770, 700)]
GREY_PIXELS = [(280, 750), (480, 580), (570, 790), (800, 715)]
APP_INSTALL_PATH = './apks/'

packages_short = ['com.goodreads']
packages_med = ['com.google.android.youtube', 'com.baidu.searchbox', 'com.amazon.mshop.android.shopping', 'com.sina.news', 'com.sohu.sohuvideo', 'com.tmall.wireless', 'com.schneeloch.tcoredirect', 'com.amazon.mshop.android.shopping', 'com.teslanet.popads', 'com.amazon.mshop.android.shopping', 'air.bv.fc2.live', 'com.google.android.apps.authenticator2', 'com.qihoo.haosou', 'cn.tianya.light', 'tv.twitch.android.app', 'com.amazon.mshop.android.shopping', 'com.alibaba.intl.android.apps.poseidon', 'bbc.mobile.news.uk', 'com.amazon.mshop.android.shopping', 'com.amazon.aws.console.mobile', 'bbc.mobile.news.uk', 'com.soundcloud.android', 'com.globo.g1.app', 'com.eg.android.alipaygphone', 'br.uol.noticias', 'com.stackexchange.marvin', 'net.ettoday.phone', 'com.zhihu.android', 'com.deviantart.android.damobile', 'com.huanqiu.hk', 'com.mediaingea.uptodown.lite', 'tv.danmaku.bili', 'com.slack', 'com.vice.viceforandroid', 'jp.nicovideo.android', 'com.shutterstock.consumer', 'com.wikihow.wikihowapp', 'asjdwe.coupons.one', 'com.amazon.mshop.android.shopping', 'com.amazon.mshop.android.shopping', 'net.danlew.gfycat', 'com.weebly.android', 'com.reimage.reimagecleaner', 'com.douban.frodo', 'com.zendesk.android', 'ru.andrikeev.android.rutrackersearch', 'com.freerange360.mpp.businessinsider', 'com.lana.webtretho', 'com.theladbible.android', 'com.softonic', 'com.upwork.android']
packages_long = ['cc.dict.dictcc', 'com.dictionary', 'com.dictionary.bn', 'com.duckduckgo.mobile.android', 'com.ebooks.ebookreader', 'com.goodreads', 'com.merriamwebster', 'com.microsoft.bing', 'com.oup.gab.odquicksearch', 'com.scribd.app.reader0', 'com.tfd.mobile.TfdSearch', 'com.urbandictionary.android', 'org.freedictionary', 'org.leo.android.dict', 'org.wikipedia', 'com.cisco.webex.meetings', 'com.citrix.saas.gotowebinar', 'com.citrixonline.android.gotomeeting', 'com.fiverr.fiverr', 'com.indeed.android.jobsearch', 'com.jobkorea.app', 'com.timesgroup.timesjobs', 'com.monster.android.Views', 'naukriApp.appModules.login', 'net.infojobs.mobile.android', 'net.slideshare.mobile', 'com.crunchyroll.crmanga', 'com.dccomics.comics', 'com.marvel.comics', 'jp.comico', 'com.cinemex', 'com.eventbrite.attendee', 'com.imbc.mini', 'com.imdb.mobile', 'com.mobile.ign', 'com.netflix.mediaclient', 'com.ninegag.android.app', 'com.sonyliv', 'com.tudou.xoom.android', 'com.vimeo.android.videoapp', 'com.wikia.singlewikia.gta', 'com.wwe.universe', 'de.tvspielfilm', 'fr.m6.m6replay', 'tv.pps.mobile', 'au.com.nab.mobile', 'br.com.bb.android', 'br.com.gabba.Caixa', 'com.aastocks.dzh', 'com.akbank.android.apps.akbank_direkt', 'com.bca', 'com.bccard.mobilecard', 'com.bradesco', 'com.garanti.cepsubesi', 'com.hanaskcard.app.touchstamp', 'com.htsu.hsbcpersonalbanking', 'com.kbcard.cxh.appcard', 'com.kbstar.kbbank', 'com.paypal.android.p2pmobile', 'com.santander.app', 'com.sbi.SBIFreedomPlus', 'com.snapwork.hdfc', 'com.vakifbank.mobile', 'com.wf.wellsfargomobile', 'com.wooribank.pib.smart', 'com.wooricard.smartapp', 'com.yahoo.mobile.client.android.finance', 'fr.creditagricole.androidapp', 'gov.irs', 'info.percentagecalculator', 'pl.mbank', 'ru.tcsbank.mcp', 'se.bankgirot.swish', 'ua.privatbank.ap24', 'au.com.realestate.app', 'com.application.zomato', 'com.appsphere.innisfreeapp', 'com.aufeminin.marmiton.activities', 'com.cookpad.android.activities', 'com.done.faasos', 'com.dubizzle.horizontal', 'com.frenys.verdadoreto', 'com.global.foodpanda.android', 'com.gumtree.android', 'com.hotornot.app', 'com.houzz.app', 'com.ikea.catalogue.android', 'com.inditex.pullandbear', 'com.inditex.zara', 'com.kt.ollehfamilybox', 'com.move.realtor', 'com.openrice.snap', 'com.redfin.android', 'com.restaurant.mobile', 'com.rightmove.android', 'com.scripps.android.foodnetwork', 'com.trulia.android', 'com.trulia.android.rentals', 'com.zoopla.activity', 'de.mcdonalds.mcdonaldsinfoapp', 'de.pixelhouse', 'ecowork.seven', 'fr.disneylandparis.android', 'jp.co.recruit.mtl.android.hotpepper', 'kr.co.station3.dabang', 'com.AnatomyLearning.Anatomy3DViewer3', 'com.anghami', 'com.bandsintown', 'com.gaana', 'com.gaana.oldhindisongs', 'com.jangomobile.android', 'com.kugou.android', 'com.mixcloud.player', 'com.musixmatch.android.lyrify', 'com.spotify.music', 'com.vevo', 'de.radio.android', 'uk.co.sevendigital.android', 'com.abc.abcnews', 'com.andrewshu.android.reddit', 'com.backelite.vingtminutes', 'com.cnn.mobile.android.phone', 'com.dailymail.online', 'com.elpais.elpais', 'com.et.reader.activities', 'com.foxnews.android', 'com.google.android.apps.genie.geniewidget', 'com.hespress.android', 'com.huffingtonpost.android', 'com.ideashower.readitlater.pro', 'com.idmedia.android.newsportal', 'com.indomedia.tabpulsa', 'com.issuu.android.app', 'com.july.ndtv', 'com.makonda.blic', 'com.mobilesrepublic.appy', 'com.newspaperdirect.pressreader.android', 'com.newspaperdirect.pressreader.android.hc', 'com.nextmedia', 'com.nextmediatw', 'com.nextradiotv.bfmtvandroid', 'com.now.newsapp', 'com.nytimes.android', 'com.sumarya', 'com.tilab', 'com.Time', 'com.toi.reader.activities', 'com.usatoday.android.news', 'com.zing.znews', 'com.zinio.mobile.android.reader', 'com.zumobi.msnbc', 'de.cellular.focus', 'de.cellular.tagesschau', 'de.heute.mobile', 'de.lineas.lit.ntv.android', 'fr.lepoint.android', 'fr.playsoft.android.tv5mondev2', 'fr.playsoft.lefigarov3', 'id.co.babe', 'in.AajTak.headlines', 'net.aljazeera.english', 'net.trikoder.android.kurir', 'org.detikcom.rss', 'ru.rian.reader', 'se.sr.android', 'uk.co.economist', 'blibli.mobile.commerce', 'br.com.dafiti', 'com.acerstore.android', 'com.alibaba.aliexpresshd', 'com.appnana.android.giftcardrewards', 'com.asda.android', 'com.asos.app', 'com.ebay.kleinanzeigen', 'com.ebay.mobile', 'com.elevenst', 'com.elevenst.deals', 'com.etsy.android', 'com.flipkart.android', 'com.geomobile.tiendeo', 'com.goldtouch.ct.yad2', 'com.groupon', 'com.hmallapp', 'com.hnsmall', 'com.homeshop18.activity', 'com.interpark.shop', 'com.jabong.android', 'com.lamoda.lite', 'com.mercadolibre', 'com.mobisoft.morhipo', 'com.myntra.android', 'com.opensooq.OpenSooq', 'com.sahibinden', 'com.shopclues', 'com.shopping.limeroad', 'com.shpock.android', 'com.snapdeal.main', 'com.souq.app', 'com.taobao.taobao', 'com.thefancy.app', 'com.wallapop', 'com.wemakeprice', 'com.wildberries.ru', 'com.zalora.android', 'com.zulily.android', 'de.sec.mobile', 'gsshop.mobile.v2', 'id.co.elevenia', 'jp.co.paperboy.minne.app', 'jp.co.rakuten.auction.android.search', 'kr.co.emart.emartmall', 'kr.co.quicket', 'kr.co.ssg', 'net.giosis.shopping.jp', 'nl.marktplaats.android', 'pl.allegro', 'ru.auto.ara', 'ru.ozon.app.android', 'ru.yandex.market', 'trendyol.com', 'co.vine.android', 'com.badoo.mobile', 'com.eharmony', 'com.facebook.katana', 'com.foursquare.robin', 'com.google.android.apps.blogger', 'com.hi5.app', 'com.imvu.mobilecordova', 'com.instagram.android', 'com.justunfollow.android', 'com.keek', 'com.linkedin.android', 'com.okcupid.okcupid', 'com.pinterest', 'com.sec.penup', 'com.sina.weibo', 'com.taggedapp', 'com.taptrip', 'com.tumblr', 'com.twitter.android', 'com.wamba.client', 'com.waplog.social', 'com.weheartit', 'jp.ameba', 'jp.mixi', 'mobi.skyrock.Skyrock', 'org.wordpress.android', 'ru.mamba.client', 'ru.mobstudio.andgalaxy', 'ru.ok.android', 'com.afl.ucom.view', 'com.bamnetworks.mobile.android.ballpark', 'com.bamnetworks.mobile.android.gameday.atbat', 'com.bleacherreport.android.teamstream', 'com.cricbuzz.android', 'com.espn.fc', 'com.espn.score_center', 'com.eurosport', 'com.fifa.fifaapp.android', 'com.fivemobile.thescore', 'com.gotv.nflgamecenter.us.lite', 'com.handmark.sportcaster', 'com.hudl.hudroid', 'com.iphonedroid.marca', 'com.july.univision', 'com.livescore', 'com.mgmbk.iddaa', 'com.mobilefootie.wc2010', 'com.myleaderboard.GolfChannel', 'com.netbiscuits.kicker', 'com.nfl.fantasy.core.android', 'com.protrade.sportacular', 'com.supersport.android.phone', 'com.televisa.deportes.android', 'com.tour.pgatour', 'com.visualdesign.livefootballontvlite', 'com.xoopsoft.apps.bundesliga.free', 'de.motain.iliga', 'kr.co.psynet', 'com.careem.acma', 'com.dailyroads.v', 'com.its.rto', 'com.mxdata.tube.Market', 'com.navitime.local.navitime', 'com.thetrainline', 'com.ubercab', 'ru.rzd', 'taxi.android.client', 'com.aa.android', 'com.accor.appli.hybrid', 'com.agoda.mobile.consumer', 'com.airasia.mobile', 'com.airbnb.android', 'com.ba.mobile', 'com.booking', 'com.cheaptickets', 'com.cleartrip.android', 'com.couchsurfing.mobile.android', 'com.delta.mobile.android', 'com.ebookers', 'com.expedia.bookings', 'com.flightaware.android.liveFlightTracker', 'com.gm.decolar', 'com.gm.despegar', 'com.goibibo', 'com.hanatour.dotcom', 'com.hcom.android', 'com.hoteltonight.android.prod', 'com.ixigo', 'com.jetblue.JetBlueAndroid', 'com.joelapenna.foursquared', 'com.justdial.search', 'com.kayak.android', 'com.korail.korail', 'com.makemytrip', 'com.momondo.flightsearch', 'com.orbitz', 'com.pagesjaunes', 'com.priceline.android.negotiator', 'com.ryanair.cheapflights', 'com.southwestairlines.mobile', 'com.traveloka.android', 'com.tripadvisor.tripadvisor', 'com.tripit', 'com.trivago', 'com.urbanspoon', 'com.xe.currency', 'com.yelp.android', 'de.flixbus.app', 'de.is24.android', 'in.redbus.android', 'jp.co.ana.android.tabidachi', 'net.skyscanner.android.main', 'com.accuweather.android', 'com.aws.android', 'com.foreca.android.weather', 'com.gismeteo.client', 'com.ilmeteo.android.ilmeteo', 'com.lachainemeteo.androidapp', 'com.palmarysoft.forecaweather', 'com.studioeleven.windfinder', 'com.supportware.Buienradar', 'com.weather.Weather', 'com.wetter.androidclient', 'de.wetteronline.regenradar', 'de.wetteronline.wetterapp', 'com.google.android.apps.youtube.creator']

def get_sub(pic, x, y):
    temp = []
    for j in range(16):
        for i in range(135):
            temp.append(pic[x+i, y+j])
    return temp

def is_all_blue(rgbvals):
    for val in rgbvals:
        if (val != BLUE):
            return False
    return True

def find_blue_rectangle(filename):
    img = Image.open(filename)
    pic = img.load()

    for j in range(150):
        for i in range(8):
            if is_all_blue(get_sub(pic, i*135, j*16)):
                print(i*135, j*16)
                return (i*135, j*16)
    return False

def check_if_app_exists(filename):
    img = Image.open(filename)
    pic = img.load()

    for coord in GREEN_PIXELS:
        if (pic[coord[0], coord[1]] != GREEN):
            return True
    
    for coord in GREY_PIXELS:
        if (pic[coord[0], coord[1]] != GREY):
            return True
        
    return False
        

def screenshot():
    try:
        subprocess.run(['adb', '-s', ID, 'shell', 'screencap', '-p', f'/storage/emulated/0/{SCREENSHOT_FILENAME}'])
        subprocess.run(['adb', '-s', ID, 'pull', f'/storage/emulated/0/{SCREENSHOT_FILENAME}'])
        subprocess.run(['adb', '-s', ID, 'shell', 'rm', f'/storage/emulated/0/{SCREENSHOT_FILENAME}'])
        return SCREENSHOT_FILENAME

    except subprocess.CalledProcessError as e:
        print(f'Screenshot function failed with exit code: {e.returncode}')
        return False

def simulate_home_key():
    subprocess.run(['adb', '-s', ID, 'shell', 'input', 'keyevent KEYCODE_HOME'])

def open_app_playstore_page(package):
    try:
        subprocess.run(['adb', '-s', ID, 'shell', 'am', 'start', '-a', 'android.intent.action.VIEW', '-d', f'market://details?id={package}'])
        return True
    
    except subprocess.CalledProcessError as e:
        print(f'Open play store for package [{package}]\r\nFunction failed with exit code: {e.returncode}')
        return False

def main():
    with alive_bar(len(packages_med)) as bar:
        for package in packages_med:
            # Check if apk already downloaded
            if (os.path.isfile(f'{APP_INSTALL_PATH}{package}.apk')):
                print(f'{package} is already downloaded - skipping')

            else:
                try:
                    # List of packages installed on device
                    installed_packages = subprocess.run(['adb', 'shell', 'pm list packages'], capture_output=True, text=True, check=True)

                    # If package not in list continue
                    if (not package in installed_packages.stdout):
                        if (open_app_playstore_page(package)):
                            time.sleep(WAIT_TIME)
                            screenshot_file = screenshot()
                            if (screenshot_file):
                                if (check_if_app_exists(screenshot_file)):
                                    coords = find_blue_rectangle(screenshot_file)

                                    # Install button found
                                    if coords:
                                        x, y = coords
                                        try:
                                            # Click install then wait for the app to download and install
                                            subprocess.run(['adb', '-s', ID, 'shell', 'input', 'tap', str(x), str(y)], check=True)
                                            time.sleep(INSTALL_WAIT_TIME)
                                        except subprocess.CalledProcessError as e:
                                            print(f'Click on play store install button failed for package [{package}]\r\nFunction failed with exit code: {e.returncode}')
                                            bar()
                                            continue
                            
                                        # Fetch apk file from device and save to local storage
                                        try:
                                            # Get device apk path
                                            result = subprocess.run(['adb', 'shell', f'pm path {package}'], capture_output=True, text=True, check=True)
                                            raw_path = result.stdout.splitlines()[0]
                                            # Remove 'package:' text from path
                                            path = raw_path[raw_path.find('package:') + len('package:'):len(raw_path)]
                                            # Save apk to local storage
                                            subprocess.run(['adb', '-s', ID, 'pull', f'{path}', f'{APP_INSTALL_PATH}{package}.apk'])
                                            # Unistall app from device
                                            subprocess.run(['adb', '-s', ID, 'uninstall', f'{package}'])
                                            os.remove(SCREENSHOT_FILENAME)
                                            bar()

                                        except subprocess.CalledProcessError as e:
                                            print(f'Failed to fetch apk from device for package [{package}]\r\nFunction failed with exit code: {e.returncode}')
                                            bar()
                                            continue

                                    else:
                                        print(f'Failed to find install button for package [{package}] - skipping')
                                        bar()
                                        continue
                                else:
                                    print(f'Package [{package}] no longer exists - skipping')
                                    bar()
                                    continue

                            else:
                                print(f'Screenshot failed for package [{package}] - skipping')
                                bar()
                                continue

                        # Failed to open play store page
                        else:
                            print(f'Failed to open play store for package [{package}] - skipping')
                            bar()
                            continue
                    
                    else:
                        print(f'{package} is already installed - skipping')
                        bar()
                        continue

                except subprocess.CalledProcessError as e:
                    print(f'Failed to find list of packages installed on device\r\nFunction failed with exit code: {e.returncode}')
                    bar()
                    continue

if __name__ == '__main__':
    main()