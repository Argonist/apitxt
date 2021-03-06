# json2htm.py is a python script to create a stand-alone HTML file with an htm extension
#
# Copyright (c) 2017-2018 Stephen E Slevinski Jr <slevin@signpuddle.net>
#
# License: MIT
#

import sys
import argparse
import glob
import json
import markdown
from pprint import pprint


##################
# Argument Setup
##################
parser = argparse.ArgumentParser(description="Create an HTML file with or without JavaScript"
	,epilog="Part of the ApiTxt project available online\nhttps://github.com/slevinski/apitxt")
parser.add_argument("-i","--input", help="name of input file")
parser.add_argument("-o","--output", metavar="filename", help="write to output file")
args = parser.parse_args()

if args.input:
	with open(args.input) as data_file:    
		data = json.load(data_file)
else:
	with sys.stdin as data_file:    
		data = json.load(data_file)

if args.output:
  sys.stdout = open(args.output,'w')

def utf8(x):
	return x.encode('utf-8')

print "<!doctype html>"
print "<html><head>"
print "  <meta charset=\"utf-8\">"
print "  <meta id=\"idviewport\" name=\"viewport\" content=\"width=device-width, user-scalable=no, initial-scale=1\">"
print "  <meta name=\"apple-mobile-web-app-capable\" content=\"yes\">"
print "  <title>SignPuddle 3</title>"
print "  <style>"
print "html,legend{box-sizing:border-box}form,svg:not(:root){overflow:hidden}button,canvas{display:inline-block}button,legend{white-space:normal}button>svg g text.sym-line,i.icon svg path{fill:currentColor!important}button,nav{text-align:center}button,section{vertical-align:middle}@font-face{font-family:SuttonSignWritingLine;src:local('SuttonSignWritingLine'),url(fonts/SuttonSignWritingLine.ttf) format('truetype')}@font-face{font-family:SuttonSignWritingFill;src:local('SuttonSignWritingFill'),url(fonts/SuttonSignWritingFill.ttf) format('truetype')}@font-face{font-family:SuttonSignWritingOneD;src:local('SuttonSignWritingOneD'),url(fonts/SuttonSignWritingOneD.ttf) format('truetype')}.sswOneD{font-family:SuttonSignWritingOneD}/*! normalize.css v7.0.0 | MIT License | github.com/necolas/normalize.css */button,hr,input{overflow:visible}progress,sub,sup{vertical-align:baseline}html{line-height:1.15;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}body{margin:0}h1{font-size:1.5em;margin:.34em 0}hr{box-sizing:content-box;height:0}pre{font-family:monospace,monospace;font-size:1em}a{-webkit-text-decoration-skip:objects}abbr[title]{border-bottom:none;text-decoration:underline;text-decoration:underline dotted}b,strong{font-weight:bolder}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative}sub{bottom:-.25em}sup{top:-.5em}button,input,optgroup,select,textarea{font-family:sans-serif;font-size:100%;line-height:1.15;margin:0}button,select{text-transform:none}[type=reset],[type=submit],button,html [type=button]{-webkit-appearance:button}[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner,button::-moz-focus-inner{border-style:none;padding:0}[type=button]:-moz-focusring,[type=reset]:-moz-focusring,[type=submit]:-moz-focusring,button:-moz-focusring{outline:ButtonText dotted 1px}fieldset{padding:.35em .75em .625em}legend{color:inherit;display:table;max-width:100%;padding:0}textarea{overflow:auto}[type=number]::-webkit-inner-spin-button,[type=number]::-webkit-outer-spin-button{height:auto}[type=search]{-webkit-appearance:textfield;outline-offset:-2px}[type=search]::-webkit-search-cancel-button,[type=search]::-webkit-search-decoration{-webkit-appearance:none}::-webkit-file-upload-button{-webkit-appearance:button;font:inherit}*,:after,:before{box-sizing:inherit}form{margin-bottom:2em}input:focus,select:focus,textarea:focus{outline:0;border:1px solid #1E6BD6}select{-webkit-appearance:none;-moz-appearance:none;line-height:1}label{font-weight:600;font-size:.9rem;display:block;margin:.5rem 0}.container{width:100%;margin:0 auto;padding:0 1rem}button{padding-bottom:.3em;font-size:1.15em;font-weight:400;-ms-touch-action:manipulation;touch-action:manipulation;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;border:1px solid transparent;border-radius:.3em;background:#EEE;color:#111;min-height:2em}button.large{font-size:1.5em;line-height:1.5em;border-radius:.3em}header button.large{margin-top:0}button:active:focus,button:focus{outline:-webkit-focus-ring-color auto 5px;outline-offset:-2px}button:focus,button:hover{color:#333;background:#DDD;text-decoration:none}button:active{background:#CCC;outline:0;-webkit-box-shadow:inset 0 3px 5px rgba(0,0,0,.125);box-shadow:inset 0 3px 5px rgba(0,0,0,.125)}button.danger:active,button.info:active,button.outline:active,button.primary:active,button.pseudo:active,button.success:active,button.warning:active{background-image:none}button.disabled,button[disabled]{cursor:not-allowed;filter:alpha(opacity=65);-webkit-box-shadow:none;box-shadow:none;opacity:.65}button.pseudo{color:#333;background-color:transparent;border-color:transparent}button.pseudo:focus,button.pseudo:hover{color:#333;background-color:#EEE}button.pseudo:active,button.pseudo:active:focus,button.pseudo:active:hover{color:#333;background-color:#DDD}button.outline,button.pseudo.disabled:focus,button.pseudo.disabled:hover,button.pseudo[disabled]:focus,button.pseudo[disabled]:hover{background-color:#fff;border-color:#ccc}button.outline{color:#333}button.outline:focus{color:#333;background-color:#e6e6e6;border-color:#8c8c8c}button.outline:active,button.outline:hover{color:#333;background-color:#e6e6e6;border-color:#adadad}button.outline:active:focus,button.outline:active:hover{color:#333;background-color:#d4d4d4;border-color:#8c8c8c}button.outline.disabled:focus,button.outline.disabled:hover,button.outline[disabled]:focus,button.outline[disabled]:hover{background-color:#fff;border-color:#ccc}button.primary{color:#fff;background-color:#337ab7;border-color:#2e6da4}button.primary:focus{color:#fff;background-color:#286090;border-color:#122b40}button.primary:active,button.primary:hover{color:#fff;background-color:#286090;border-color:#204d74}button.primary:active:focus,button.primary:active:hover{color:#fff;background-color:#204d74;border-color:#122b40}button.primary.disabled:hover,button.primary[disabled]:hover{background-color:#337ab7;border-color:#2e6da4}button.success{color:#fff;background-color:#5cb85c;border-color:#4cae4c}button.success:focus{color:#fff;background-color:#449d44;border-color:#255625}button.success:active,button.success:hover{color:#fff;background-color:#449d44;border-color:#398439}button.success:active:focus,button.success:active:hover{color:#fff;background-color:#398439;border-color:#255625}button.success.disabled:focus,button.success.disabled:hover,button.success[disabled]:focus,button.success[disabled]:hover{background-color:#5cb85c;border-color:#4cae4c}button.info{color:#fff;background-color:#5bc0de;border-color:#46b8da}button.info:focus{color:#fff;background-color:#31b0d5;border-color:#1b6d85}button.info:active,button.info:hover{color:#fff;background-color:#31b0d5;border-color:#269abc}button.info:active:focus,button.info:active:hover{color:#fff;background-color:#269abc;border-color:#1b6d85}button.info.disabled:focus,button.info.disabled:hover,button.info[disabled]:focus,button.info[disabled]:hover{background-color:#5bc0de;border-color:#46b8da}button.warning{color:#fff;background-color:#f0ad4e;border-color:#eea236}button.warning:focus{color:#fff;background-color:#ec971f;border-color:#985f0d}button.warning:active,button.warning:hover{color:#fff;background-color:#ec971f;border-color:#d58512}button.warning:active:focus,button.warning:active:hover{color:#fff;background-color:#d58512;border-color:#985f0d}button.warning.disabled:focus,button.warning.disabled:hover,button.warning[disabled]:focus,button.warning[disabled]:hover{background-color:#f0ad4e;border-color:#eea236}button.danger{color:#fff;background-color:#d9534f;border-color:#d43f3a}button.danger:focus{color:#fff;background-color:#c9302c;border-color:#761c19}button.danger:active,button.danger:hover{color:#fff;background-color:#c9302c;border-color:#ac2925}button.danger:active:focus,button.danger:active:hover{color:#fff;background-color:#ac2925;border-color:#761c19}button.danger.disabled:focus,button.danger.disabled:hover,button.danger[disabled]:focus,button.danger[disabled]:hover{background-color:#d9534f;border-color:#d43f3a}button.link{font-weight:400;color:#337ab7;border-radius:0}button.link,button.link:active,button.link[disabled]{background-color:transparent;-webkit-box-shadow:none;box-shadow:none}button.link,button.link:active,button.link:focus,button.link:hover{border-color:transparent}button.link:focus,button.link:hover{color:#23527c;text-decoration:underline;background-color:transparent}button.link[disabled]:focus,button.link[disabled]:hover{color:#777;text-decoration:none}input,select,textarea{display:block;padding:.5rem;background:0 0;width:100%;max-width:100%;border:1px solid #cdcdcd;border-radius:4px;font-size:.95rem}button i.icon,button img.icon,i.icon svg{width:1em;height:1em;position:relative}input.primary,select.primary,textarea.primary{border:1px solid #337ab7}input.success,select.success,textarea.success{border:1px solid #5cb85c}input.info,select.info,textarea.info{border:1px solid #5bc0de}input.warning,select.warning,textarea.warning{border:1px solid #f0ad4e}input.danger,select.danger,textarea.danger{border:1px solid #d9534f}button i.icon,button img.icon{margin-right:.3em;top:.1em}button>svg{position:relative;width:1.3em;height:1.3em;top:.2em}button>svg g text.sym-fill{fill:#eee!important}button.outline>svg g text.sym-fill{fill:#fff!important}button.primary>svg g text.sym-fill{fill:#337ab7!important}button.success>svg g text.sym-fill{fill:#5cb85c!important}button.info>svg g text.sym-fill{fill:#5bc0de!important}button.warning>svg g text.sym-fill{fill:#f0ad4e!important}button.danger>svg g text.sym-fill{fill:#d9534f!important}button.link>svg g text.sym-fill{fill:#fff!important}button[disabled]{fill:#bbb!important}.invalid{box-shadow:0 0 5px #d45252;border-color:#b03535}button.thin{margin-left:0;margin-right:0}button.onLeft,div.onLeft{float:left}button.onRight,div.onRight{float:right}header{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;background:#d3d3d3;margin-bottom:1em;height:3em}@media (min-width:30em){header{grid-template-columns:1fr 2fr 1fr 1fr;grid-gap:1em}}@media (min-width:50em){header{grid-template-columns:1fr 4fr 1fr 1fr}}header button{margin-top:.3em}button.brand{color:#b33}nav{line-height:3em}nav button{margin-left:.5em;margin-right:.5em}button.message{display:block;margin:.5em;max-width:780px;width:80%}button.message i{float:left}section{margin:1em auto;padding:.5em 1em 1em;max-width:780px;width:90%;min-height:75px;background:#FFF}section.boxed{position:relative;box-shadow:0 1px 4px rgba(0,0,0,.3),0 0 40px rgba(0,0,0,.1) inset}section.boxed:after,section.boxed:before{content:\"\";position:absolute;z-index:-1;box-shadow:0 0 20px rgba(0,0,0,.8);top:0;bottom:0;left:10px;right:10px;border-radius:100px/10px}section.boxed:after{right:10px;left:auto;transform:skew(8deg) rotate(3deg)}section button{margin:.5em}button.long{display:none}.tight{padding:.1em}input.swu{font-size:2em}@media (min-width:30em){button.long{display:initial}button.short{display:none}div.label,label{float:left;width:28%;clear:both;vertical-align:middle}div.wide,input{float:right;width:72%}h2{clear:both}form button{float:left}}"
print "h1.brand {"
print "  color: #b33;"
print "}"
print "header.three {"
print "  display: grid;"
print "  grid-template-columns: 1fr 3fr 1fr;"
print "  background: lightgray;"
print "  margin-bottom: 1em;"
print "  height: 3em;"
print "}"
print "@media (min-width: 30em) {"
print "  header.three {"
print "    grid-template-columns: 1fr 4fr 1fr;"
print "    grid-gap: 1em;"
print "  }"
print "}"
print "@media (min-width: 50em) {"
print "  header.three {"
print "    grid-template-columns: 1fr 5fr 1fr;"
print "  }"
print "}"
print "  </style>"
print "</head>"
print "<body>"
print "  <header class=\"three\">"
print "    <div></div>"
print "    <h1 class=\"brand\">"
print "      <i class=\"icon\">"
print "        <svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 382.39499 393.798\"><g transform=\"translate(-153.728 -166.677)\"><path fill=\"#000\" d=\"M348.22 266.68v259.504h-7V266.68\"></path></g><g transform=\"translate(-153.728 -166.677)\"><path fill=\"#000\" d=\"M348.22 166.677v32.32h-7v-32.32\"></path></g><g transform=\"translate(-153.728 -166.677)\"><linearGradient id=\"c\" gradientUnits=\"userSpaceOnUse\" x1=\"138.098\" y1=\"180.746\" x2=\"536.098\" y2=\"375.746\"><stop offset=\"0\" stop-color=\"#ff0700\"></stop><stop offset=\"1\" stop-color=\"#b40000\"></stop></linearGradient><path d=\"M198.26 300.806c18.388 0 35.327 6.168 48.89 16.532 13.56-10.364 30.5-16.532 48.887-16.532s35.326 6.168 48.888 16.532c13.562-10.364 30.5-16.532 48.888-16.532 18.387 0 35.326 6.168 48.89 16.532 13.56-10.364 30.5-16.532 48.888-16.532 16.467 0 31.773 4.948 44.533 13.423-27.962-78.602-103-134.882-191.197-134.882-88.196 0-163.236 56.28-191.198 134.88 12.76-8.475 28.066-13.422 44.533-13.422z\" fill=\"url(#c)\"></path></g></svg>"
print "      </i>SignPuddle 3"
print "    </h1>"
print "    <div></div>"
print "  </header>"

print "    <section class=\"boxed\">"
print "        <h1>Settings</h1>"
print "        <hr>"
print "        <h2>settings.state.title</h2>"
print "        <form><label for=\"state\">settings.state.status</label><input disabled=\"\" id=\"state\" type=\"text\" class=\"warning\"><label></label>"
print "            <div class=\"wide\"><button class=\"primary sswOneD\">Initial</button><button class=\"success sswOneD\">Save</button><button class=\"outline sswOneD\">Restore</button><button class=\"outline sswOneD\">Forget</button></div>"
print "        </form>"
print "        <hr>"
print "        <h2>Server</h2>"
print "        <form><label for=\"server\">Server URL</label><input id=\"server\" type=\"text\" class=\"danger\"><label></label>"
print "            <div class=\"wide\"><button class=\"warning sswOneD\">Reset Connection</button></div>"
print "        </form>"
print "        <hr>"
print "        <h2>Country</h2>"
print "        <form><i class=\"icon\"><svg viewBox=\"0 0 1792 1792\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M896 128q209 0 385.5 103t279.5 279.5 103 385.5-103 385.5-279.5 279.5-385.5 103-385.5-103-279.5-279.5-103-385.5 103-385.5 279.5-279.5 385.5-103zm274 521q-2 1-9.5 9.5t-13.5 9.5q2 0 4.5-5t5-11 3.5-7q6-7 22-15 14-6 52-12 34-8 51 11-2-2 9.5-13t14.5-12q3-2 15-4.5t15-7.5l2-22q-12 1-17.5-7t-6.5-21q0 2-6 8 0-7-4.5-8t-11.5 1-9 1q-10-3-15-7.5t-8-16.5-4-15q-2-5-9.5-10.5t-9.5-10.5q-1-2-2.5-5.5t-3-6.5-4-5.5-5.5-2.5-7 5-7.5 10-4.5 5q-3-2-6-1.5t-4.5 1-4.5 3-5 3.5q-3 2-8.5 3t-8.5 2q15-5-1-11-10-4-16-3 9-4 7.5-12t-8.5-14h5q-1-4-8.5-8.5t-17.5-8.5-13-6q-8-5-34-9.5t-33-.5q-5 6-4.5 10.5t4 14 3.5 12.5q1 6-5.5 13t-6.5 12q0 7 14 15.5t10 21.5q-3 8-16 16t-16 12q-5 8-1.5 18.5t10.5 16.5q2 2 1.5 4t-3.5 4.5-5.5 4-6.5 3.5l-3 2q-11 5-20.5-6t-13.5-26q-7-25-16-30-23-8-29 1-5-13-41-26-25-9-58-4 6-1 0-15-7-15-19-12 3-6 4-17.5t1-13.5q3-13 12-23 1-1 7-8.5t9.5-13.5.5-6q35 4 50-11 5-5 11.5-17t10.5-17q9-6 14-5.5t14.5 5.5 14.5 5q14 1 15.5-11t-7.5-20q12 1 3-17-5-7-8-9-12-4-27 5-8 4 2 8-1-1-9.5 10.5t-16.5 17.5-16-5q-1-1-5.5-13.5t-9.5-13.5q-8 0-16 15 3-8-11-15t-24-8q19-12-8-27-7-4-20.5-5t-19.5 4q-5 7-5.5 11.5t5 8 10.5 5.5 11.5 4 8.5 3q14 10 8 14-2 1-8.5 3.5t-11.5 4.5-6 4q-3 4 0 14t-2 14q-5-5-9-17.5t-7-16.5q7 9-25 6l-10-1q-4 0-16 2t-20.5 1-13.5-8q-4-8 0-20 1-4 4-2-4-3-11-9.5t-10-8.5q-46 15-94 41 6 1 12-1 5-2 13-6.5t10-5.5q34-14 42-7l5-5q14 16 20 25-7-4-30-1-20 6-22 12 7 12 5 18-4-3-11.5-10t-14.5-11-15-5q-16 0-22 1-146 80-235 222 7 7 12 8 4 1 5 9t2.5 11 11.5-3q9 8 3 19 1-1 44 27 19 17 21 21 3 11-10 18-1-2-9-9t-9-4q-3 5 .5 18.5t10.5 12.5q-7 0-9.5 16t-2.5 35.5-1 23.5l2 1q-3 12 5.5 34.5t21.5 19.5q-13 3 20 43 6 8 8 9 3 2 12 7.5t15 10 10 10.5q4 5 10 22.5t14 23.5q-2 6 9.5 20t10.5 23q-1 0-2.5 1t-2.5 1q3 7 15.5 14t15.5 13q1 3 2 10t3 11 8 2q2-20-24-62-15-25-17-29-3-5-5.5-15.5t-4.5-14.5q2 0 6 1.5t8.5 3.5 7.5 4 2 3q-3 7 2 17.5t12 18.5 17 19 12 13q6 6 14 19.5t0 13.5q9 0 20 10t17 20q5 8 8 26t5 24q2 7 8.5 13.5t12.5 9.5l16 8 13 7q5 2 18.5 10.5t21.5 11.5q10 4 16 4t14.5-2.5 13.5-3.5q15-2 29 15t21 21q36 19 55 11-2 1 .5 7.5t8 15.5 9 14.5 5.5 8.5q5 6 18 15t18 15q6-4 7-9-3 8 7 20t18 10q14-3 14-32-31 15-49-18 0-1-2.5-5.5t-4-8.5-2.5-8.5 0-7.5 5-3q9 0 10-3.5t-2-12.5-4-13q-1-8-11-20t-12-15q-5 9-16 8t-16-9q0 1-1.5 5.5t-1.5 6.5q-13 0-15-1 1-3 2.5-17.5t3.5-22.5q1-4 5.5-12t7.5-14.5 4-12.5-4.5-9.5-17.5-2.5q-19 1-26 20-1 3-3 10.5t-5 11.5-9 7q-7 3-24 2t-24-5q-13-8-22.5-29t-9.5-37q0-10 2.5-26.5t3-25-5.5-24.5q3-2 9-9.5t10-10.5q2-1 4.5-1.5t4.5 0 4-1.5 3-6q-1-1-4-3-3-3-4-3 7 3 28.5-1.5t27.5 1.5q15 11 22-2 0-1-2.5-9.5t-.5-13.5q5 27 29 9 3 3 15.5 5t17.5 5q3 2 7 5.5t5.5 4.5 5-.5 8.5-6.5q10 14 12 24 11 40 19 44 7 3 11 2t4.5-9.5 0-14-1.5-12.5l-1-8v-18l-1-8q-15-3-18.5-12t1.5-18.5 15-18.5q1-1 8-3.5t15.5-6.5 12.5-8q21-19 15-35 7 0 11-9-1 0-5-3t-7.5-5-4.5-2q9-5 2-16 5-3 7.5-11t7.5-10q9 12 21 2 7-8 1-16 5-7 20.5-10.5t18.5-9.5q7 2 8-2t1-12 3-12q4-5 15-9t13-5l17-11q3-4 0-4 18 2 31-11 10-11-6-20 3-6-3-9.5t-15-5.5q3-1 11.5-.5t10.5-1.5q15-10-7-16-17-5-43 12zm-163 877q206-36 351-189-3-3-12.5-4.5t-12.5-3.5q-18-7-24-8 1-7-2.5-13t-8-9-12.5-8-11-7q-2-2-7-6t-7-5.5-7.5-4.5-8.5-2-10 1l-3 1q-3 1-5.5 2.5t-5.5 3-4 3 0 2.5q-21-17-36-22-5-1-11-5.5t-10.5-7-10-1.5-11.5 7q-5 5-6 15t-2 13q-7-5 0-17.5t2-18.5q-3-6-10.5-4.5t-12 4.5-11.5 8.5-9 6.5-8.5 5.5-8.5 7.5q-3 4-6 12t-5 11q-2-4-11.5-6.5t-9.5-5.5q2 10 4 35t5 38q7 31-12 48-27 25-29 40-4 22 12 26 0 7-8 20.5t-7 21.5q0 6 2 16z\"></path></svg></i><input autocomplete=\"off\" id=\"country_temp\" type=\"text\" class=\"primary\"><label></label>"
print "            <div class=\"wide\"><button class=\"primary sswOneD\">system.buttons.viewall</button></div>"
print "        </form>"
print "        <hr>"
print "        <h2>settings.language.title</h2>"
print "        <form><input autocomplete=\"off\" id=\"language_temp\" type=\"text\" class=\"primary\"><label></label>"
print "            <div class=\"wide\"><button class=\"primary sswOneD\">system.buttons.viewall</button></div>"
print "        </form>"
print "    </section>"
print "    <section class=\"boxed\">"
print "        <h2>settings.system.messages</h2>"
print "        <section class=\"boxed\"><button class=\"danger onRight sswOneD\"><i class=\"icon\"><svg viewBox=\"0 0 1792 1792\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M1490 1322q0 40-28 68l-136 136q-28 28-68 28t-68-28l-294-294-294 294q-28 28-68 28t-68-28l-136-136q-28-28-28-68t28-68l294-294-294-294q-28-28-28-68t28-68l136-136q28-28 68-28t68 28l294 294 294-294q28-28 68-28t68 28l136 136q28 28 28 68t-28 68l-294 294 294 294q28 28 28 68z\"></path></svg></i></button><button class=\"message danger sswOneD\"><i class=\"icon\"><svg viewBox=\"0 0 1792 1792\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M883 1056q0 13-10 23l-332 332 144 144q19 19 19 45t-19 45-45 19h-448q-26 0-45-19t-19-45v-448q0-26 19-45t45-19 45 19l144 144 332-332q10-10 23-10t23 10l114 114q10 10 10 23zm781-864v448q0 26-19 45t-45 19-45-19l-144-144-332 332q-10 10-23 10t-23-10l-114-114q-10-10-10-23t10-23l332-332-144-144q-19-19-19-45t19-45 45-19h448q26 0 45 19t19 45z\"></path></svg></i>Status 0 (No Response)</button></section>"
print "    </section>"

root = {}
route = ''
parameters = {}
for segment in data:

	if 'root' in segment:
		root = segment
		print "    <section class=\"boxed\">"
		print "        <h1>" + root['title'] + "</h1>"
		print "        <hr>"
		print "        <h2>" + root['root'] + "</h2>"
		if "lines" in root:
			lines = "\n".join(root['lines'])
			print markdown.markdown(lines)
		else:
			print "nothing more"
		print "</section>"

	elif 'group' in segment:
		print "// ## Group " + segment['group']
		try:
			pass
			tlines = segment['description'].split("\n")
			for tline in tlines:
				print "// " + tline
		except:
			pass

	elif 'route' in segment:
		pass
		route = segment['route']
		if 'parameters' in segment:
			parameters = segment['parameters']
		else:
			parameters = {}
	
	elif 'method' in segment:
		params = []
		queries = []
		routing = route
		try:
			while True:
				start = routing.index("{")
				end = routing.index("}")
				param = routing[start:end+1]
				if param[1]=="?":
					routing = routing.replace(param,'')
					queries = param[1:-1].replace("?","").split(",")
				else:
					routing = routing.replace(param,":" + param[1:-1])
					params.append(param[1:-1])
		except:
			pass

		try:
			vars = ",".join(["$" + p for p in params])
		except:
			vars = ''

		print "$app->get('" + routing + "', function (" + vars + ") use ($app) {"
		for query in queries:
			print "  $" + query + " = $app->request()->get('" + query + "');"
		print "  $timein = microtime(true);"
		try:
			print "  $app->contentType('" + segment['dialog'][0]['responses'][0]['type'] + "');"
		except:
			pass
		print "  $searchTime = searchtime($timein);"
		print "  header('Search-Time: ' . $searchTime);"
		if "code" in segment:
			for bline in segment['code']:
				pass
				print "  " + bline
		else:
			try:
				for bline in segment['dialog'][0]['responses'][0]['lines']:
					pass
					print "  echo '" + bline.replace("'","\\'") + "' . \"\\n\";"
			except:
				pass
		print "});"

print "</body>"
print "</html>"
