#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
@Author Amit Joshi
'''

import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf8') 

def txt_to_list(text):
	text = text.replace("।", "").replace("?", "").replace(",", "").strip()
	text = text.split(" ")

	stop_words = ['अमेरिका','घले','अर्को','अर्की','अर्का','अहिले','पहिले','कहिले','ऐले','भूमिका','चस्मा','राजीनामा','चस्मा','सम्हाले','धम्की','डरधम्की','मामा','साधुमामा','बिच्छुकी','मिले','पातकी','काका','शङ्का','बेलुका','वास्तवमा','बालिका','थाले','आमा','विश्वकर्मा','फर्की','लामा','धम्की','निको','मुलुकी','शङ्का','अमेरिकी','बेलुकी','चले','पहिले','अर्को','ढोका','शर्मा','कार्की','मर्का','ढले','टाउको','जम्मा','अर्का','झिकी','पहिले','वाटिका','गोठाले','मङ्गले','कहिले','हाले','सन्तुष्टात्मा','ढुकढुकी','अर्का','इलाका','उपत्यका','सीमा','ताका','बिथोले','टीको','खाले','अहिले','टाउका','फड्को','ओर्ले','एकअर्का','नथाकी','अँगाले','अँगाले','क्षमा','लड्की','बाँकी','ब्रह्मा','परिक्रमा','यसैले','टाउको','थाले','आमा','ठूलीआमा','खित्का','झर्को','बेलुकी','बेलुका','तहल्का','सिनेमा','नमिलाई','तालिका','उपत्यका','कास्की','मतपेटिका','पेटिका','त्यसैले','ढोका','अमेरिका	 अमेरिकी','पक्कै','आयोजना','एकै','पक्का','खित्का','टिका','बित्तिकै','देखावटी','घुड्का','जुनसुकै','खुइले','खातिर','चलाकी','योजना','गरीमा','छक्का','मुक्का','चर्को','महात्मा','अंशुवर्मा','फन्को','चर्काचर्की','सिर्जना','ढिको','घोर्ले','आत्मा','एकअर्का','शङ्का','झोंक्का','पैले','सिलाई','नायिका','हुक्का','बालिका','बुढापाका','आर्को','मिलाई','अन्तरात्मा','पेले','प्रतिमा','फुले','झझल्को','मुट्की','कशिका','जम्मा','टेकी','रूघाखोकी','द्वारिका','यशोबर्मा','फुकी','घले','इलाका','प्रसङ्ग','अभिव्यञ्जना','व्यञ्जना','चर्को','भूमिका','मानवात्मा','विश्‍वात्मा','प्रेतात्मा','महिमा','अँगाले','खड्का','सुष्मा','महिमा','सुइँको','बर्मा','ठीकै','धोका','भाले','मौका','धक्का','छिमेकी','स्वाभाविकै','निक्कै','धोका','पीरमर्का','आशङका','विकसित','अभिसारिका','देउकी','चकचकी','जमर्को','स्वभाविकै','तामा','हल्का','खुलाई','वेलुका','पोको','बोका','हल्ले','खोकी','पोले','जिवात्मा','ग्रसित','अणिमा','गरिमा','कोशिका','भोको','निकै','हाकाहाकी','सुकै','विकसित','तर्जुमा','व्यवस्थापिका','नजिकै','आयोजना','चन्द्रमा','उमा','कालिका','कनिका','एमाले','बालबालिका','पत्रिका','काफ्ले','शिक्षिका','गाउँले','सन्की','जीबिका','खसाले','पत्रपत्रिका','बेकम्मा','पिरोले','उचाले','प्याकप्याकी','खेमा','विधायिका','पहिले','जतिसुकै','बोकी','टक्का','अनुशासित','चलाई','श्रीलङ्का','चौकी','वित्तिकै','पुस्तिका','खड्का','ढुलमुले','गण्डकी','प्रसङ्ग','फलाको','ठेक्का','वर्मा','जलाई','पाका','सरक्कै','उपशंका','गुरुमा','लालिमा','विवश','अफ्रिकी','अफ्रिका','कालीगण्डकी','बोलाई','झाँकी','बोले','हुरूक्‍कै','वेलुका','कैले','चोथाले','जैले','भुड्को','साले','भुतुक्‍कै','सुटुक्‍कै','सीको','धोको','ठिकै','बाँकी','इराकी','तरिका','डोको','डोका','डोले','खोले','तरीका','परमात्मा','मुचुल्का','बोको','बान्की','निस्की','चर्कै','चर्की','चर्का','शतवार्षिकी','शासित','श्रीलङ्का','हलुका','त्यसताका','पटुकी','जुलाई','अहिले','भित्रिएको','घटेको', 'र', 'पनि', 'भने', 'नै', 'छन्', 'केही', 'त']

	for word in text:
		if word in stop_words:
			text.remove(word)

	return text