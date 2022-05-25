from codigo.NReinasInd import NReinasInd

import os
import calendar
import time

class Tablero () :

    def __init__ ( self, ind : NReinasInd ) :
        self.__individuo = ind
        self.__startHtml ( )

    def __getStyle ( self ) :
        return """
        * {
            padding : 0;
            margin : 0;
        }
        body {
            background-image : linear-gradient(to right, #2E0249, #A91079);
        }
        .tablero {
            position: absolute;
            width : 500px;
            height : 500px;
            border : 10px solid #468759; 
            top: 50%;
            left: 50%;
            -ms-transform: translate(-50%, -50%);
            transform: translate(-50%, -50%);
            -webkit-box-shadow: 33px 14px 111px -8px rgba(122,122,122,1);
            -moz-box-shadow: 33px 14px 111px -8px rgba(122,122,122,1);
            box-shadow: 33px 14px 111px -8px rgba(122,122,122,1);
        }
        table tr td img {
            width : 80px;
            border : 0;
        }
        table tr td {
            width : 80px;
            height : 80px;
            border : none;
        }     
        .claro {
            background-color : #14C38E;
        }   
        .escuro {
            background-color : #B8F1B0;
        }
        """

    def __startHtml ( self ) :
        self.__baseHtml =  '<html><head><title>{}-Reinas</title>'.format(str(self.__individuo.nReinas))
        self.__baseHtml += '<style>{}</style></head><body>'.format(self.__getStyle())

    def __closeHtml ( self ) :
        self.__baseHtml += '</body></html>'

    def gerarImagem ( self, pathToSave : str = './output' ) :
        url_queen = '../assets/queen.png'
        self.__baseHtml += "<table class='tablero'>"
        cont = 0
        for i in range( self.__individuo.nReinas ) :
            self.__baseHtml += "<tr>"
            for ind in  self.__individuo.genes :
                self.__baseHtml += "<td class='{}'>".format( 'escuro' if cont % 2 == 0 else 'claro' )                
                self.__baseHtml += "<img src='{}'>".format(url_queen) if ind == i else '&nbsp;'
                self.__baseHtml += "</td>"
                cont += 1
            if self.__individuo.nReinas % 2 == 0 :
                cont += 1
            self.__baseHtml += "</tr>"
        self.__baseHtml += "</table>"
        self.__closeHtml()
        if not os.path.isdir ( pathToSave ) :
            os.makedirs ( pathToSave )
        name = 'tablero-{}-Reinas-{}.html'.format( str(self.__individuo.nReinas), str(calendar.timegm(time.gmtime())))
        _file = open(os.path.join( pathToSave, name ), 'w')
        print('tablero salvo em {}'.format(os.path.abspath(os.path.join(pathToSave, name))))
        _file.write(self.__baseHtml)
        _file.close()
        return os.path.abspath(os.path.join(pathToSave, name))