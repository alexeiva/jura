#MenuTitle: Set Kerning Groups for GF Latin Plus
# encoding: utf-8
# Copyright: Georg Seifert, 2010, www.schriftgestaltung.de Version 1.0
# Copyright: Alexei Vanyashin, 2016, www.cyreal.org Version 1.01
# This script is derived from Georg Seifert's 'Set Kerning Groups located at 'https://github.com/schriftgestalt/Glyphs-Scripts/blob/master/Metrics%20%26%20Classes/set%20Kerning%20Groups.py
# It is reworked to include kerning classes for GF Latin Plus Encoding. 
 
import sys
import os
from GlyphsApp import *
import objc
from AppKit import *
from Foundation import *
import traceback

Keys = [
	"A",
	"B",
	"C",
	"D",
	"E",
	"F",
	"G",
	"H",
	"I",
	"J",
	"K",
	"L",
	"M",
	"N",
	"O",
	"P",
	"Q",
	"R",
	"S",
	"T",
	"U",
	"V",
	"W",
	"X",
	"Y",
	"Z",
	"Agrave",
	"Aacute",
	"Acircumflex",
	"Atilde",
	"Adieresis",
	"Amacron",
	"Abreve",
	"Aring",
	"Aringacute",
	"Adotbelow",
	"Aogonek",
	"AE",
	"AEacute",
	"Cacute",
	"Ccircumflex",
	"Ccaron",
	"Cdotaccent",
	"Ccedilla",
	"Dcaron",
	"Dcroat",
	"Eth",
	"Egrave",
	"Eacute",
	"Ecircumflex",
	"Etilde",
	"Ecaron",
	"Edieresis",
	"Emacron",
	"Ebreve",
	"Edotaccent",
	"Edotbelow",
	"Eogonek",
	"Gcircumflex",
	"Gcaron",
	"Gbreve",
	"Gdotaccent",
	"Gcommaaccent",
	"Hcircumflex",
	"Hbar",
	"Igrave",
	"Iacute",
	"Icircumflex",
	"Itilde",
	"Idieresis",
	"Imacron",
	"Ibreve",
	"Idotaccent",
	"Idotbelow",
	"Iogonek",
	"Jcircumflex",
	"Kcommaaccent",
	"Lacute",
	"Lcaron",
	"Lcommaaccent",
	"Lslash",
	"Ldot",
	"Nacute",
	"Ntilde",
	"Ncaron",
	"Ncommaaccent",
	"Eng",
	"Ograve",
	"Oacute",
	"Ocircumflex",
	"Otilde",
	"Odieresis",
	"Omacron",
	"Obreve",
	"Ohungarumlaut",
	"Odotbelow",
	"Oogonek",
	"Oslash",
	"Oslashacute",
	"OE",
	"Racute",
	"Rcaron",
	"Rcommaaccent",
	"Sacute",
	"Scircumflex",
	"Scaron",
	"Scedilla",
	"Scommaaccent",
	"Germandbls",
	"Tcaron",
	"Tcedilla",
	"Tcommaaccent",
	"Tbar",
	"Thorn",
	"Ugrave",
	"Uacute",
	"Ucircumflex",
	"Utilde",
	"Udieresis",
	"Umacron",
	"Ubreve",
	"Uring",
	"Uhungarumlaut",
	"Udotbelow",
	"Uogonek",
	"Wgrave",
	"Wacute",
	"Wcircumflex",
	"Wdieresis",
	"Ygrave",
	"Yacute",
	"Ycircumflex",
	"Ytilde",
	"Ydieresis",
	"Ymacron",
	"Zacute",
	"Zcaron",
	"Zdotaccent",
	"Schwa",
	"DZcaron",
	"Dzcaron",
	"LJ",
	"Lj",
	"NJ",
	"Nj",
	"Adblgrave",
	"Ainvertedbreve",
	"Edblgrave",
	"Einvertedbreve",
	"Idblgrave",
	"Iinvertedbreve",
	"Odblgrave",
	"Oinvertedbreve",
	"Rdblgrave",
	"Rinvertedbreve",
	"Udblgrave",
	"Uinvertedbreve",
	"Odieresismacron",
	"Otildemacron",
	"Odotaccentmacron",
	"Abreveacute",
	"Abrevedotbelow",
	"Abrevegrave",
	"Abrevehookabove",
	"Abrevetilde",
	"Acircumflexacute",
	"Acircumflexdotbelow",
	"Acircumflexgrave",
	"Acircumflexhookabove",
	"Acircumflextilde",
	"Ahookabove",
	"Ecircumflexacute",
	"Ecircumflexdotbelow",
	"Ecircumflexgrave",
	"Ecircumflexhookabove",
	"Ecircumflextilde",
	"Ehookabove",
	"Ocircumflexacute",
	"Ocircumflexdotbelow",
	"Ocircumflexgrave",
	"Ocircumflexhookabove",
	"Ocircumflextilde",
	"Ohookabove",
	"Ohorn",
	"Ohornacute",
	"Ohorndotbelow",
	"Ohorngrave",
	"Ohornhookabove",
	"Ohorntilde",
	"Uhookabove",
	"Uhorn",
	"Uhornacute",
	"Uhorndotbelow",
	"Uhorngrave",
	"Uhornhookabove",
	"Uhorntilde",
	"Ydotbelow",
	"Yhookabove",
	"Ihookabove",
	"I_J.loclNLD",
	"Iacute_J.loclNLD",
	"a",
	"aacute",
	"abreve",
	"abreveacute",
	"abrevedotbelow",
	"abrevegrave",
	"abrevehookabove",
	"abrevetilde",
	"acircumflex",
	"acircumflexacute",
	"acircumflexdotbelow",
	"acircumflexgrave",
	"acircumflexhookabove",
	"acircumflextilde",
	"adblgrave",
	"adieresis",
	"adotbelow",
	"agrave",
	"ahookabove",
	"ainvertedbreve",
	"amacron",
	"aogonek",
	"aring",
	"aringacute",
	"atilde",
	"ae",
	"aeacute",
	"b",
	"c",
	"cacute",
	"ccaron",
	"ccedilla",
	"ccircumflex",
	"cdotaccent",
	"d",
	"eth",
	"dcaron",
	"dcroat",
	"dz",
	"dzcaron",
	"e",
	"eacute",
	"ebreve",
	"ecaron",
	"ecircumflex",
	"ecircumflexacute",
	"ecircumflexdotbelow",
	"ecircumflexgrave",
	"ecircumflexhookabove",
	"ecircumflextilde",
	"edblgrave",
	"edieresis",
	"edotaccent",
	"edotbelow",
	"egrave",
	"ehookabove",
	"einvertedbreve",
	"emacron",
	"eogonek",
	"etilde",
	"f",
	"g",
	"gbreve",
	"gcaron",
	"gcircumflex",
	"gcommaaccent",
	"gdotaccent",
	"h",
	"hbar",
	"hcircumflex",
	"i",
	"idotless",
	"iacute",
	"ibreve",
	"icircumflex",
	"idblgrave",
	"idieresis",
	"idotaccent",
	"idotbelow",
	"igrave",
	"ihookabove",
	"iinvertedbreve",
	"imacron",
	"iogonek",
	"itilde",
	"j",
	"jdotless",
	"jcircumflex",
	"k",
	"kcommaaccent",
	"kgreenlandic",
	"l",
	"lacute",
	"lcaron",
	"lcommaaccent",
	"ldot",
	"lj",
	"lslash",
	"m",
	"n",
	"nacute",
	"ncaron",
	"ncommaaccent",
	"eng",
	"nj",
	"ntilde",
	"o",
	"oacute",
	"obreve",
	"ocircumflex",
	"ocircumflexacute",
	"ocircumflexdotbelow",
	"ocircumflexgrave",
	"ocircumflexhookabove",
	"ocircumflextilde",
	"odblgrave",
	"odieresis",
	"odieresismacron",
	"odotaccentmacron",
	"odotbelow",
	"ograve",
	"ohookabove",
	"ohorn",
	"ohornacute",
	"ohorndotbelow",
	"ohorngrave",
	"ohornhookabove",
	"ohorntilde",
	"ohungarumlaut",
	"oinvertedbreve",
	"omacron",
	"oogonek",
	"oslash",
	"oslashacute",
	"otilde",
	"otildemacron",
	"oe",
	"p",
	"thorn",
	"q",
	"r",
	"racute",
	"rcaron",
	"rcommaaccent",
	"rdblgrave",
	"rinvertedbreve",
	"s",
	"sacute",
	"scaron",
	"scedilla",
	"scircumflex",
	"scommaaccent",
	"germandbls",
	"schwa",
	"t",
	"tbar",
	"tcaron",
	"tcedilla",
	"tcommaaccent",
	"u",
	"uacute",
	"ubreve",
	"ucircumflex",
	"udblgrave",
	"udieresis",
	"udotbelow",
	"ugrave",
	"uhookabove",
	"uhorn",
	"uhornacute",
	"uhorndotbelow",
	"uhorngrave",
	"uhornhookabove",
	"uhorntilde",
	"uhungarumlaut",
	"uinvertedbreve",
	"umacron",
	"uogonek",
	"uring",
	"utilde",
	"v",
	"w",
	"wacute",
	"wcircumflex",
	"wdieresis",
	"wgrave",
	"x",
	"y",
	"yacute",
	"ycircumflex",
	"ydieresis",
	"ydotbelow",
	"ygrave",
	"yhookabove",
	"ymacron",
	"ytilde",
	"z",
	"zacute",
	"zcaron",
	"zdotaccent",
	"f_f",
	"f_f_i",
	"f_f_ij",
	"f_f_l",
	"f_ij",
	"fi",
	"fl",
	"i_j.loclNLD",
	"iacute_j.loclNLD",
	"ordfeminine",
	"ordmasculine",
	"onehalf",
	"onequarter",
	"threequarters",
	"asterisk",
	"backslash",
	"periodcentered",
	"bullet",
	"colon",
	"comma",
	"ellipsis",
	"exclam",
	"exclamdown",
	"numbersign",
	"period",
	"question",
	"questiondown",
	"quotedbl",
	"quotesingle",
	"semicolon",
	"slash",
	"underscore",
	"periodcentered.loclCAT",
	"braceleft",
	"braceright",
	"bracketleft",
	"bracketright",
	"parenleft",
	"parenright",
	"braceleft.case",
	"braceright.case",
	"bracketleft.case",
	"bracketright.case",
	"parenleft.case",
	"parenright.case",
	"emdash",
	"endash",
	"hyphen",
	"softhyphen",
	"guillemetleft",
	"guillemetright",
	"guilsinglleft",
	"guilsinglright",
	"quotedblbase",
	"quotedblleft",
	"quotedblright",
	"quoteleft",
	"quoteright",
	"quotesinglbase",
	"cedi",
	"cent",
	"colonsign",
	"currency",
	"dollar",
	"dong",
	"euro",
	"florin",
	"franc",
	"guarani",
	"kip",
	"lira",
	"liraTurkish",
	"manat",
	"naira",
	"peseta",
	"peso",
	"ruble",
	"rupeeIndian",
	"sterling",
	"won",
	"yen",
	"bulletoperator",
	"divisionslash",
	"plus",
	"minus",
	"multiply",
	"divide",
	"equal",
	"notequal",
	"greater",
	"less",
	"greaterequal",
	"lessequal",
	"plusminus",
	"approxequal",
	"asciitilde",
	"logicalnot",
	"micro",
	"percent",
	"perthousand",
	"at",
	"ampersand",
	"paragraph",
	"section",
	"copyright",
	"registered",
	"trademark",
	"degree",
	"bar",
	"brokenbar",
	"dagger",
	"daggerdbl",
	"numero",
	"asciicircum",
### End GF Latin Plus list
### Start Greek
	"Alpha",
	"Beta",
	"Gamma",
	"Delta",
	"Epsilon",
	"Zeta",
	"Eta",
	"Theta",
	"Iota",
	"Kappa",
	"Lambda",
	"Mu",
	"Nu",
	"Omicron",
	"Pi",
	"Rho",
	"Tau",
	"Upsilon",
	"Chi",
	"Alphatonos",
	"Epsilontonos",
	"Etatonos",
	"Iotatonos",
	"Iotadieresis",
	"Omicrontonos",
	"Upsilontonos",
	"Upsilondieresis",
	"Omegatonos",
	"beta",
	"eta",
	"kappa",
	"mu",
	"omicron",
	"rho",
	"sigma",
	"psi",
	"alphatonos",
	"epsilontonos",
	"etatonos",
	"iotadieresis",
	"omicrontonos",
	"upsilontonos",
	"upsilondieresistonos",
	"upsilondieresis",
	"omegatonos",
### End Greek
	]
	
DefaultKeys = {
	"A : ["A","A"],
	"B : ["H","B"],
	"C : ["O","C"],
	"D : ["H","O"],
	"E : ["H","E"],
	"F : ["H","F"],
	"G : ["O","C"],
	"H : ["H","H"],
	"I : ["H","H"],
	"J : ["J","J"],
	"K : ["H","K"],
	"L : ["H","L"],
	"M : ["H","H"],
	"N : ["H","H"],
	"O : ["O","O"],
	"P : ["H","P"],
	"Q : ["O","O"],
	"R : ["H","R"],
	"S : ["S","S"],
	"T : ["T","T"],
	"U : ["U","U"],
	"V : ["V","V"],
	"W : ["V","V"],
	"X : ["X","X"],
	"Y : ["V","V"],
	"Z : ["Z","Z"],
	"Agrave : ["A","A"],
	"Aacute : ["A","A"],
	"Acircumflex : ["A","A"],
	"Atilde : ["A","A"],
	"Adieresis : ["A","A"],
	"Amacron : ["A","A"],
	"Abreve : ["A","A"],
	"Aring : ["A","A"],
	"Aringacute : ["A","A"],
	"Adotbelow : ["A","A"],
	"Aogonek : ["A","A"],
	"AE : ["A","E"],
	"AEacute : ["A","E"],
	"Cacute : ["O","C"],
	"Ccircumflex : ["O","C"],
	"Ccaron : ["O","C"],
	"Cdotaccent : ["O","C"],
	"Ccedilla : ["O","C"],
	"Dcaron : ["H","O"],
	"Dcroat : ["Hbar","O"],
	"Eth : ["Hbar","E"],
	"Egrave : ["H","E"],
	"Eacute : ["H","E"],
	"Ecircumflex : ["H","E"],
	"Etilde : ["H","E"],
	"Ecaron : ["H","E"],
	"Edieresis : ["H","E"],
	"Emacron : ["H","E"],
	"Ebreve : ["H","E"],
	"Edotaccent : ["H","E"],
	"Edotbelow : ["H","E"],
	"Eogonek : ["H","E"],
	"Gcircumflex : ["O","C"],
	"Gcaron : ["O","C"],
	"Gbreve : ["O","C"],
	"Gdotaccent : ["O","C"],
	"Gcommaaccent : ["O","C"],
	"Hcircumflex : ["H","H"],
	"Hbar : ["H","H"],
	"Igrave : ["H","H"],
	"Iacute : ["H","H"],
	"Icircumflex : ["H","H"],
	"Itilde : ["H","H"],
	"Idieresis : ["H","H"],
	"Imacron : ["H","H"],
	"Ibreve : ["H","H"],
	"Idotaccent : ["H","H"],
	"Idotbelow : ["H","H"],
	"Iogonek : ["H","H"],
	"Jcircumflex : ["J","J"],
	"Kcommaaccent : ["H","K"],
	"Lacute : ["H","L"],
	"Lcaron : ["H","L"],
	"Lcommaaccent : ["H","L"],
	"Lslash : ["H","L"],
	"Ldot : ["H","L"],
	"Nacute : ["H","H"],
	"Ntilde : ["H","H"],
	"Ncaron : ["H","H"],
	"Ncommaaccent : ["H","H"],
	"Eng : ["H","H"],
	"Ograve : ["O","O"],
	"Oacute : ["O","O"],
	"Ocircumflex : ["O","O"],
	"Otilde : ["O","O"],
	"Odieresis : ["O","O"],
	"Omacron : ["O","O"],
	"Obreve : ["O","O"],
	"Ohungarumlaut : ["O","O"],
	"Odotbelow : ["O","O"],
	"Oogonek : ["O","O"],
	"Oslash : ["O","O"],
	"Oslashacute : ["O","O"],
	"OE : ["O","E"],
	"Racute : ["H","R"],
	"Rcaron : ["H","R"],
	"Rcommaaccent : ["H","R"],
	"Sacute : ["S","S"],
	"Scircumflex : ["S","S"],
	"Scaron : ["S","S"],
	"Scedilla : ["S","S"],
	"Scommaaccent : ["S","S"],
	"Germandbls : ["H","Germandbls"],
	"Tcaron : ["T","T"],
	"Tcedilla : ["T","T"],
	"Tcommaaccent : ["T","T"],
	"Tbar : ["T","T"],
	"Thorn : ["T","T"],
	"Ugrave : ["U","U"],
	"Uacute : ["U","U"],
	"Ucircumflex : ["U","U"],
	"Utilde : ["U","U"],
	"Udieresis : ["U","U"],
	"Umacron : ["U","U"],
	"Ubreve : ["U","U"],
	"Uring : ["U","U"],
	"Uhungarumlaut : ["U","U"],
	"Udotbelow : ["U","U"],
	"Uogonek : ["U","U"],
	"Wgrave : ["V","V"],
	"Wacute : ["V","V"],
	"Wcircumflex : ["V","V"],
	"Wdieresis : ["V","V"],
	"Ygrave : ["Y","Y"],
	"Yacute : ["Y","Y"],
	"Ycircumflex : ["Y","Y"],
	"Ytilde : ["Y","Y"],
	"Ydieresis : ["Y","Y"],
	"Ymacron : ["Y","Y"],
	"Zacute : ["Z","Z"],
	"Zcaron : ["Z","Z"],
	"Zdotaccent : ["Z","Z"],
	"Schwa : ["S","S"],
	"DZcaron : ["H","Z"],
	"Dzcaron : ["H","Z"],
	"LJ : ["H","J"],
	"Lj : ["H","j"],
	"NJ : ["H","J"],
	"Nj : ["N","j"],
	"Adblgrave : ["A","A"],
	"Ainvertedbreve : ["A","A"],
	"Edblgrave : ["H","E"],
	"Einvertedbreve : ["H","E"],
	"Idblgrave : ["H","H"],
	"Iinvertedbreve : ["H","H"],
	"Odblgrave : ["O","O"],
	"Oinvertedbreve : ["O","O"],
	"Rdblgrave : ["H","R"],
	"Rinvertedbreve : ["H","R"],
	"Udblgrave : ["U","U"],
	"Uinvertedbreve : ["U","U"],
	"Odieresismacron : ["O","O"],
	"Otildemacron : ["O","O"],
	"Odotaccentmacron : ["O","O"],
	"Abreveacute : ["A","A"],
	"Abrevedotbelow : ["A","A"],
	"Abrevegrave : ["A","A"],
	"Abrevehookabove : ["A","A"],
	"Abrevetilde : ["A","A"],
	"Acircumflexacute : ["A","A"],
	"Acircumflexdotbelow : ["A","A"],
	"Acircumflexgrave : ["A","A"],
	"Acircumflexhookabove : ["A","A"],
	"Acircumflextilde : ["A","A"],
	"Ahookabove : ["A","A"],
	"Ecircumflexacute : ["H","E"],
	"Ecircumflexdotbelow : ["H","E"],
	"Ecircumflexgrave : ["H","E"],
	"Ecircumflexhookabove : ["H","E"],
	"Ecircumflextilde : ["H","E"],
	"Ehookabove : ["H","E"],
	"Ocircumflexacute : ["O","O"],
	"Ocircumflexdotbelow : ["O","O"],
	"Ocircumflexgrave : ["O","O"],
	"Ocircumflexhookabove : ["O","O"],
	"Ocircumflextilde : ["O","O"],
	"Ohookabove : ["O","O"],
	"Ohorn : ["O","O"],
	"Ohornacute : ["O","O"],
	"Ohorndotbelow : ["O","O"],
	"Ohorngrave : ["O","O"],
	"Ohornhookabove : ["O","O"],
	"Ohorntilde : ["O","O"],
	"Uhookabove : ["U","U"],
	"Uhorn : ["U","U"],
	"Uhornacute : ["U","U"],
	"Uhorndotbelow : ["U","U"],
	"Uhorngrave : ["U","U"],
	"Uhornhookabove : ["U","U"],
	"Uhorntilde : ["U","U"],
	"Ydotbelow : ["Y","Y"],
	"Yhookabove : ["Y","Y"],
	"Ihookabove : ["H","H"],
	"I_J.loclNLD" : ["H", "J"],
	"Iacute_J.loclNLD" : ["H", "J"],
	"a : ["a","n"],
	"aacute : ["a","n"],
	"abreve : ["a","n"],
	"abreveacute : ["a","n"],
	"abrevedotbelow : ["a","n"],
	"abrevegrave : ["a","n"],
	"abrevehookabove : ["a","n"],
	"abrevetilde : ["a","n"],
	"acircumflex : ["a","n"],
	"acircumflexacute : ["a","n"],
	"acircumflexdotbelow : ["a","n"],
	"acircumflexgrave : ["a","n"],
	"acircumflexhookabove : ["a","n"],
	"acircumflextilde : ["a","n"],
	"adblgrave : ["a","n"],
	"adieresis : ["a","n"],
	"adotbelow : ["a","n"],
	"agrave : ["a","n"],
	"ahookabove : ["a","n"],
	"ainvertedbreve : ["a","n"],
	"amacron : ["a","n"],
	"aogonek : ["a","n"],
	"aring : ["a","n"],
	"aringacute : ["a","n"],
	"atilde : ["a","n"],
	"ae : ["a","e"],
	"aeacute : ["a","e"],
	"b : ["h","o"],
	"c : ["o","c"],
	"cacute : ["o","c"],
	"ccaron : ["o","c"],
	"ccedilla : ["o","c"],
	"ccircumflex : ["o","c"],
	"cdotaccent : ["o","c"],
	"d : ["o","d"],
	"eth : ["o","o"],
	"dcaron : ["o","d"],
	"dcroat : ["o","d"],
	"dz : ["o","z"],
	"dzcaron : ["o","z"],
	"e : ["e","e"],
	"eacute : ["o","e"],
	"ebreve : ["o","e"],
	"ecaron : ["o","e"],
	"ecircumflex : ["o","e"],
	"ecircumflexacute : ["o","e"],
	"ecircumflexdotbelow : ["o","e"],
	"ecircumflexgrave : ["o","e"],
	"ecircumflexhookabove : ["o","e"],
	"ecircumflextilde : ["o","e"],
	"edblgrave : ["o","e"],
	"edieresis : ["o","e"],
	"edotaccent : ["o","e"],
	"edotbelow : ["o","e"],
	"egrave : ["o","e"],
	"ehookabove : ["o","e"],
	"einvertedbreve : ["o","e"],
	"emacron : ["o","e"],
	"eogonek : ["o","e"],
	"etilde : ["o","e"],
	"f : ["f","f"],
	"g : ["g","g"],
	"gbreve : ["g","g"],
	"gcaron : ["g","g"],
	"gcircumflex : ["g","g"],
	"gcommaaccent : ["g","g"],
	"gdotaccent : ["g","g"],
	"h : ["h","n"],
	"hbar : ["h","n"],
	"hcircumflex : ["h","n"],
	"i : ["i","i"],
	"idotless : ["n","u"],
	"iacute : ["i","i"],
	"ibreve : ["i","i"],
	"icircumflex : ["i","i"],
	"idblgrave : ["i","i"],
	"idieresis : ["i","i"],
	"idotaccent : ["i","i"],
	"idotbelow : ["i","i"],
	"igrave : ["i","i"],
	"ihookabove : ["i","i"],
	"iinvertedbreve : ["i","i"],
	"imacron : ["i","i"],
	"iogonek : ["i","i"],
	"itilde : ["i","i"],
	"j : ["j","j"],
	"jdotless : ["jdotless","idotless"],
	"jcircumflex : ["j","j"],
	"k : ["h","k"],
	"kcommaaccent : ["h","k"],
	"kgreenlandic : ["n","k"],
	"l : ["h","l"],
	"lacute : ["h","l"],
	"lcaron : ["h","l"],
	"lcommaaccent : ["h","l"],
	"ldot : ["h","l"],
	"lj : ["h","l"],
	"lslash : ["hbar","l"],
	"m : ["n","n"],
	"n : ["n","n"],
	"nacute : ["n","n"],
	"ncaron : ["n","n"],
	"ncommaaccent : ["n","n"],
	"eng : ["n","j"],
	"nj : ["n","j"],
	"ntilde : ["n","n"],
	"o : ["o","o"],
	"oacute : ["o","o"],
	"obreve : ["o","o"],
	"ocircumflex : ["o","o"],
	"ocircumflexacute : ["o","o"],
	"ocircumflexdotbelow : ["o","o"],
	"ocircumflexgrave : ["o","o"],
	"ocircumflexhookabove : ["o","o"],
	"ocircumflextilde : ["o","o"],
	"odblgrave : ["o","o"],
	"odieresis : ["o","o"],
	"odieresismacron : ["o","o"],
	"odotaccentmacron : ["o","o"],
	"odotbelow : ["o","o"],
	"ograve : ["o","o"],
	"ohookabove : ["o","o"],
	"ohorn : ["o","o"],
	"ohornacute : ["o","o"],
	"ohorndotbelow : ["o","o"],
	"ohorngrave : ["o","o"],
	"ohornhookabove : ["o","o"],
	"ohorntilde : ["o","o"],
	"ohungarumlaut : ["o","o"],
	"oinvertedbreve : ["o","o"],
	"omacron : ["o","o"],
	"oogonek : ["o","o"],
	"oslash : ["o","o"],
	"oslashacute : ["o","o"],
	"otilde : ["o","o"],
	"otildemacron : ["o","o"],
	"oe : ["o","e"],
	"p : ["p","o"],
	"thorn : ["h","o"],
	"q : ["o","q"],
	"r : ["n","r"],
	"racute : ["n","r"],
	"rcaron : ["n","r"],
	"rcommaaccent : ["n","r"],
	"rdblgrave : ["n","r"],
	"rinvertedbreve : ["n","r"],
	"s : ["s","s"],
	"sacute : ["s","s"],
	"scaron : ["s","s"],
	"scedilla : ["s","s"],
	"scircumflex : ["s","s"],
	"scommaaccent : ["s","s"],
	"germandbls : ["h","germandbls"],
	"schwa : ["o","o"],
	"t : ["t","t"],
	"tbar : ["t","t"],
	"tcaron : ["t","t"],
	"tcedilla : ["t","t"],
	"tcommaaccent : ["t","t"],
	"u : ["u","u"],
	"uacute : ["u","u"],
	"ubreve : ["u","u"],
	"ucircumflex : ["u","u"],
	"udblgrave : ["u","u"],
	"udieresis : ["u","u"],
	"udotbelow : ["u","u"],
	"ugrave : ["u","u"],
	"uhookabove : ["u","u"],
	"uhorn : ["u","u"],
	"uhornacute : ["u","u"],
	"uhorndotbelow : ["u","u"],
	"uhorngrave : ["u","u"],
	"uhornhookabove : ["u","u"],
	"uhorntilde : ["u","u"],
	"uhungarumlaut : ["u","u"],
	"uinvertedbreve : ["u","u"],
	"umacron : ["u","u"],
	"uogonek : ["u","u"],
	"uring : ["u","u"],
	"utilde : ["u","u"],
	"v : ["v","v"],
	"w : ["v","v"],
	"wacute : ["v","v"],
	"wcircumflex : ["v","v"],
	"wdieresis : ["v","v"],
	"wgrave : ["v","v"],
	"x : ["x","x"],
	"y : ["y","y"],
	"yacute : ["y","y"],
	"ycircumflex : ["y","y"],
	"ydieresis : ["y","y"],
	"ydotbelow : ["y","y"],
	"ygrave : ["y","y"],
	"yhookabove : ["y","y"],
	"ymacron : ["y","y"],
	"ytilde : ["y","y"],
	"z : ["z","z"],
	"zacute : ["z","z"],
	"zcaron : ["z","z"],
	"zdotaccent : ["z","z"],
	"f_f" : ["f", "f"],
	"f_f_i" : ["f", "i"],
	"f_f_ij" : ["f", "j"],
	"f_f_l" : ["f", "l"],
	"f_ij" : ["f", "j"],
	"fi" : ["f", "i"],
	"fl" : ["f", "l"],
	"i_j.loclNLD" : ["i", "j"],
	"iacute_j.loclNLD" : ["i", "j"],
	"ordfeminine" : ["ordfeminine", "ordfeminine"],
	"ordmasculine" : ["ordfeminine", "ordfeminine"],
	"onehalf" : ["onehalf", "onehalf"],
	"onequarter" : ["onehalf", "onehalf"],
	"threequarters" : ["onehalf", "onehalf"],
### Greek	
	"Alpha" : ["A", "A"],
	"Beta" : ["H", "B"],
	"Gamma" : ["", "H"],
	"Delta" : ["A", "A"],
	"Epsilon" : ["H", "E"],
	"Zeta" : ["Z", "Z"],
	"Eta" : ["H", "H"],
	"Theta" : ["O", "O"],
	"Iota" : ["H", "H"],
	"Kappa" : ["H", "K"],
	"Lambda" : ["A", "A"],
	"Mu" : ["M", "M"],
	"Nu" : ["H", "H"],
	"Omicron" : ["O", "O"],
	"Pi" : ["H", "H"],
	"Rho" : ["H", "P"],
	"Tau" : ["T", "T"],
	"Upsilon" : ["Y", "Y"],
	"Chi" : ["X", "X"],
	"Alphatonos" : ["A", "A"],
	"Epsilontonos" : ["E", "E"],
	"Etatonos" : ["H", "H"],
	"Iotatonos" : ["H", "H"],
	"Iotadieresis" : ["H", "H"],
	"Omicrontonos" : ["O", "O"],
	"Upsilontonos" : ["Y", "Y"],
	"Upsilondieresis" : ["Y", "Y"],
	"Omegatonos" : ["Omega", "Omega"],
	"beta" : ["h", ""],
	"eta" : ["n", "n"],
	"kappa" : ["n", "k"],
	"mu" : ["p", "u"],
	"omicron" : ["o", "o"],
	"rho" : ["rho", "o"],
	"sigma" : ["o", ""],
	"psi" : ["upsilon", "upsilon"],
	"alphatonos" : ["alpha", "alpha"],
	"epsilontonos" : ["epsilon", "epsilon"],
	"etatonos" : ["n", "n"],
	"iotadieresis" : ["i", "i"],
	"omicrontonos" : ["o", "o"],
	"upsilontonos" : ["upsilon", "upsilon"],
	"upsilondieresistonos" : ["upsilon", "upsilon"],
	"upsilondieresis" : ["upsilon", "upsilon"],
	"omegatonos" : ["omega", "omega"],
}

def KeysForGlyph(Glyph):
	if Glyph == None:
		return []
	global DefaultKeys
	LeftKey = False
	RightKey = False
	try:
		LeftKey = Glyph.leftKerningGroup
	except:
		print traceback.format_exc()
	try:
		RightKey = Glyph.rightKerningGroup
	except:
		print traceback.format_exc()
	try:
		if len(LeftKey < 1):
			LeftKey = False
	except TypeError:
		pass
	except:
		print traceback.format_exc()
	try:
		if len(RightKey < 1):
			RightKey = False
	except TypeError:
		pass
	except:
		print traceback.format_exc()
	return (LeftKey, RightKey)

def updateKeyGlyphsForSelected():
	Doc = Glyphs.currentDocument
	Font = Doc.font
	SelectedLayers = Doc.selectedLayers()
	for Layer in SelectedLayers:
		Glyph = Layer.parent
		LeftKey = ""
		RightKey = ""
		LigatureComponents = Glyph.name.split("_")
		if len(Layer.components) > 0 and len(Layer.paths) == 0 and Layer.components[0].transformStruct()[0] == 1:
			componentGlyph = Layer.components[0].component
			if not componentGlyph:
				raise Exception("Something is wrong with a Component in Glyphs %s" % Layer.parent.name)
			if componentGlyph.category == "Letter":
				LeftKey = KeysForGlyph(componentGlyph)[0]
			if not LeftKey:
				LeftKey = componentGlyph.name
			
			for Component in Layer.components:
				try:
					if Component.component.category == "Letter":
						if Component.transform[0] == 1:
							componentGlyph = Component.component
					elif Component.component.category != "Mark":
						#componentGlyph = None
						pass
				except:
					pass
			if componentGlyph:
				RightKey = KeysForGlyph(componentGlyph)[1]
				if not RightKey:
					RightKey = componentGlyph.name
		
		elif len(LigatureComponents) > 1:
			LeftGlyph = Font.glyphs[LigatureComponents[0]]
			if LeftGlyph != None:
				LeftKey = KeysForGlyph(LeftGlyph)[0]
			RightGlyph = Font.glyphs[LigatureComponents[-1]]
			if RightGlyph != None:
				RightKey = KeysForGlyph(RightGlyph)[1]
		if LeftKey:
			try:
				if LeftKey not in Font.glyphs and not Font.glyphs[LeftKey].export:
					LeftKey = False
			except:
				LeftKey = False
		if RightKey:
			try:
				if RightKey not in Font.glyphs and not Font.glyphs[RightKey].export:
					RightKey = False
			except:
				pass
		if not LeftKey:
			try:
				LeftKey = DefaultKeys[Glyph.name][0]
			except KeyError:
				pass
			except:
				print traceback.format_exc()
		if not RightKey:
			try:
				RightKey = DefaultKeys[Glyph.name][1]
			except KeyError:
				pass
			except:
				print traceback.format_exc()
		if not LeftKey and Glyph.name[-3:] == ".sc":
			try:
				Glyph
				LeftKey = DefaultKeys[Glyph.name[:-3].title()][0]
				if (len(LeftKey) > 0):
					LeftKey = LeftKey.lower()+".sc"
			except:
				print traceback.format_exc()
		if not RightKey and Glyph.name[-3:] == ".sc":
			try:
				RightKey = DefaultKeys[Glyph.name[:-3].title()][1]
				if (len(RightKey) > 0):
					RightKey = RightKey.lower()+".sc"
			except:
				print traceback.format_exc()
		if not LeftKey:
			LeftKey = Glyph.name
		if not RightKey:
			RightKey = Glyph.name
		
		print Glyph.name, ">", LeftKey, RightKey
		if Glyph.leftKerningGroup is None or len(Glyph.leftKerningGroup) == 0:
			Glyph.setLeftKerningGroup_(LeftKey)
		if Glyph.rightKerningGroup is None or len(Glyph.rightKerningGroup) == 0:
			Glyph.setRightKerningGroup_(RightKey)

def main():
 	print "*** Start Update Key Glyphs ***\n"
	updateKeyGlyphsForSelected()
	print "*** Ende ****"
	
def test():
	NewDefaultKeys = {}
	for key in Keys:
		key = niceName(key)
		values = DefaultKeys[key]
		newValues = []
		for value in values:
			newValues.append( niceName(value) )
		print "	\"%s\" : [\"%s\", \"%s\"]," % (key, newValues[1], newValues[0])
		NewDefaultKeys[key] = newValues
	#print NewDefaultKeys
main()

#test()