# -*- coding: utf-8 -*-
import json
import re
import os
import urllib
import csv
import subprocess
from subprocess import Popen, PIPE, check_call

mobtrackers = ['Inmobi', 'Mopub', 'Facebook', 'Chartboost', 'Crashlytics', 'Heyzap', 'Applovin', 'Unitytechnologies', 'Vungle', 'Fyber', 'Millenialmedia', 'Ironsource', 'Tapjoy', 'Flurry', 'Google', 'Bitstadium', 'Presage', 'Comscore', 'Umeng', 'Tencent', 'Nexage', 'Mixpanel', 'Appboy', 'Yandex', 'Kochava', 'Urbanairship', 'Daum', 'Milkman', 'Playhaven', 'Umeng', 'Mail.Ru', 'Newrelic', 'Admob', 'Moat', 'Smaato', 'Admarvel', 'Appodeal', 'Cauley', 'Revmob', 'Adbuddiz', 'Igaworks', 'Nativex', 'Smartadserver', 'Mobfox', 'Pubnative', 'Hyprmx', 'Pingstart', 'Tune', 'Baidu', 'Swrve', 'Tnkfactory', 'Appnext', 'Tencent']
webtrackers = ['Google', 'Doubleclick', 'Facebook', 'Cloudfront', 'Scorecardresearch', 'Appnexus', 'Twitter', 'Amazon', 'Criteo', 'Yahoo', 'Oracle', 'Quantcast', 'Iponweb', 'Adobe', 'Openx', 'Ghostery', 'Rubicon', 'Bluekai', 'Cloudflare', 'Liveramp', 'The Nielsen Company', 'Demdex', 'Truste', 'Newrelic', 'Integral Ad Science', 'Adsrvr', 'Moatads', 'Pubmatic', 'Turn', 'Indexchange', 'Doubleverify', 'Mathtag', 'Chartbeat', 'Optimizely', 'Youtube', 'Tapad', 'Exelate', 'Targus', 'Lotame', 'Sizmek', 'Iasds', 'Neustar', 'Jquery', 'Krxd', 'Adroll', 'Brightroll', 'Audiencescience', 'Bootstrap', 'Rocketfuel', 'Dataxu', 'Tubemogul', 'Microsoft', 'Yandex', 'Conversant', 'Videology', 'Flashtalking', 'Akamai', 'Adap.Tv', 'Magnetic', 'Dstillery', 'Baidu', 'Smartadserver', 'Taboola', 'H&R Block', 'Tealium', 'Convertro', 'MSN', 'Linkedin', 'Mookie1', 'Contextweb', 'Liverail', 'Yadro', 'Bug', 'Chango', 'Conversant Llc', 'Trueffect', 'Signal-Privacy', 'Crazy Egg', 'Drawbridge Inc', 'Sovrn', 'Ovh', 'Exponential', 'Yieldoptimizer', 'Spotxchange', 'Owneriq', 'Insightexpress', 'Adform', 'Automattic', 'Disqus', 'Outbrain', 'Flipps', 'Centromedia', 'Ignitionone', 'Skimlinks', 'Simpli.Fi', 'Wordpress', 'Openx Technologies', 'Ensighten', 'Visual Website Optimizer', 'Rhythmone', 'Mixpanel', 'Sonobi', 'Hotjar', 'Voicefive', 'Gssprt', 'At Internet', 'Ml314', 'Radiumone', 'Parsely', 'Improve Digital Bv', 'Gumgum', 'Amgdgt', 'Effective Measure', 'Pinterest', 'Vk', 'Adition', 'Exoclick', 'Ixi Corporation', 'Nugg.Ad', 'Umeng', 'Alibaba', 'Marketo', 'Gskinner', 'Gigya', 'Tns', 'Eq Works', 'Cxense Asa', 'Steelhouse', 'Yieldlab', '33Across', 'Mail.Ru', 'Pingdom Ab', 'Smart Adserver', 'Brightcove', 'Postrelease', 'Adriver', 'Pagefair', 'Microad', 'Marin Software', 'Collective', 'Trafficjunky', 'Pixalate', 'Demandbase', 'Yieldbot', 'Visualdna', 'Ioam', 'Signal', 'Shopzilla', 'Sharethrough', 'Rambler', 'Clicktale', 'Sociomantic', 'Datonics', 'Run', 'Myspace', 'Taobao', 'Adgear Technologies', 'Sharethis', 'Mybuys', 'Stroeer Media', 'The Mcgraw-Hill Companies', 'Vizury', 'Abc', 'Dyn', 'Longtail Ad Solutions', 'Netseer', 'Smaato', 'The Adex Gmbh', 'Adblade', 'Mxptint', 'Maxymiser', 'Admeta', 'Mcro', 'Sourcepoint Technologies', 'Yieldmanager', 'Rfihub', 'Bounce Exchange', 'Wtp', 'Convertmedia', 'Rackspace Us', 'Eyeview', 'Qualtrics', 'Intent Iq', 'Stickyads.Tv', 'Soasta', 'Cedexis Inc', 'Weborama', 'Invite Media', 'Histats', 'Statcounter', 'Paypal', 'Bidr', 'Springserve', 'Yahoo', 'Nexstar Broadcasting', 'Triplelift', 'Polar', 'Adelphic Inc', 'Deep Forest Media', 'Cedexis', 'Richrelevance', 'Resonate', 'Impact-Ad', 'Jivox', 'Mediade', 'Liveperson', 'Zedo', 'Yabidos', 'Adfox', 'Fout', 'Switch', 'Navegg S.A.', 'Adsnative', 'Eyeota Limited', 'Jsdelivr', 'Consumerinfo.Com', 'Brandscreen Pty Ltd', 'Mythings', 'Polar Mobile Group', 'Answercloud', 'Komoona', 'Admeta', 'Meltdsp', 'Appier Inc', 'Netdna', 'Budgetedbauer', 'Gfk', 'Bidtheatre', 'Research Now', 'Undertone Networks', 'Viglink', 'Adbrain', 'Adstir', 'Sailthru', 'Vimeo', 'Mediametrie', 'Livefyre', 'Mediaforge', 'Webklipper', 'Tencent', 'Ib-Ibi']
trackers = set(mobtrackers)|set(webtrackers)
obj  = json.load(open('../data/company_details.json', encoding='utf-8'))
toptrackers = obj.copy()
for tracker in trackers:
	try:
		if toptrackers[tracker]["id"] not in trackers:
			toptrackers.pop(tracker)
	except KeyError:
		print(f"key [{tracker}] not found")
		continue

for tracker in toptrackers:
	domains = toptrackers[tracker]["domains"]
	fulldomains = filter(None, domains)
	toptrackers[tracker]["domains"] = fulldomains

def getDomainCo(host):
	for tracker in toptrackers:
		for domain in toptrackers[tracker]["domains"]:
			if domain in host:
				return toptrackers[tracker]["id"]

# open the text file which is output of grep, record any recognised domains in the output.json file

def recordTrackers(apkname, urlsname):
	urls = open(urlsname).read()
	trackers = []
	for tracker in toptrackers:
		for domain in toptrackers[tracker]["domains"]:
			if str(domain) in urls:
				trackers.append(str(tracker))
	trackers = list(set(trackers))
	print(trackers)
	irrelevant = ["app", "identity", "n/a", "other", "", "library"]
	for tracker in trackers:
		for cat in irrelevant:
			if (obj[tracker]["typetag"] == cat):
				trackers.remove(tracker)
				print('removed %s because %s' % (tracker, obj[tracker]["typetag"]))
	print(trackers)
	line = '"%s": %s,' % (apkname, json.dumps(trackers))
	output.write(line)

# # toptrackers = getPopTrackers()

output = open('output_testing.json', 'a')

# selected apps version

for filename in test_apps:
	print(filename)
	fullpath = (directory + filename)
	print(fullpath)
	# os.system("apktool d %s.apk" % fullpath)
	unpackedname = filename.rsplit( ".", 1 )[ 0 ]
	urlsname = "%s_urls.txt" % filename
	# os.system(f'rg "https?://[^ >]+" %s > %s' % (filename, urlsname))
	# print(f'rg "https?://[^ >]+" {directory}{filename} > {urlsname}')
	# os.system(f'rg "https?://[^ >]+" {directory}{filename} > {urlsname}')
	# os.system('rg "https?://[^ >]+" %s > %s' % (filename, urlsname))
#	os.system('grep -Er "iponweb" %s > %s' % (filename, urlsname))
#	os.system("grep -Er %s %s > %s" % ("http://\K[^']+", filename, urlsname))
	# recordTrackers(filename,urlsname)

	os.system(f'rd /s /q E:\\PROWISH-app-decompile\\test-apks\\{filename}')
	# os.system(f'rd {urlsname}')

	# os.system("rm -r %s" % filename)
	# os.system("rm %s" % urlsname)
	

def main():
	pass

if __name__ == '__main__':
    main()