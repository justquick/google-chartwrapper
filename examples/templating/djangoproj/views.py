# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response


def example(request):
    greek_elections = [
        { 'type': 'Pie3D',
            'title': 'Greek Elections 2009',
            'data': [43.92, 33.48, 7.54, 5.63, 4.60, 2.53, 2.3],
            'labels': 'ΠΑΣΟΚ|ΝΔ|ΚΚΕ|ΛΑΟΣ|ΣΥΡΙΖΑ|Οικολόγοι Πράσινοι|Λοιποί',
            'colors': '0ab927|005ac0|ff0000|100077|ffd000|99cc33|888888'
        },
        { 'type': 'Pie3D',
            'title': 'Greek Elections 2007',
            'data': [41.83, 38.10, 8.15, 5.04, 3.80, 1.05, 2.03],
            'labels': 'ΝΔ|ΠΑΣΟΚ|ΚΚΕ|ΣΥΡΙΖΑ|ΛΑΟΣ|Οικολόγοι Πράσινοι|Λοιποί',
            'colors': '005ac0|0ab927|ff0000|ffd000|100077|99cc33|888888'
        },
        { 'type': 'Pie3D',
            'title': 'Greek Elections 2004',
            'data': [45.4, 40.5, 5.9, 3.3, 2.2, 1.8, 0.9],
            'labels': 'ΝΔ|ΠΑΣΟΚ|ΚΚΕ|ΣΥΡΙΖΑ|ΛΑΟΣ|ΔΗΚΚΙ|Λοιποί',
            'colors': '005ac0|0ab927|ff0000|ffd000|100077|ff7f00|888888'
        }
    ]
    for g in greek_elections: 
        g['legend'] = map(unicode, g['data'])
        
 
    return render_to_response('example.html',{
        'venndata': [100,80,60,30,30,30,10],
        'piedata':[60,40],
        'bhgdata':['el','or'],
        '20q': ['Animals','Vegetables','Minerals'],
        'qrstr':'''To the human eye QR Codes look like hieroglyphics, 
            but they can be read by any device that has 
            the appropriate software installed.''',
        'temps':'max 25°|min 15°',
        'elections': greek_elections
        })
