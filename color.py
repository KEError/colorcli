#color set
def set(text,color,bg='black',style='normal'):
    _colorDirectory={
        'black':'30',
        'red':'31',
        'green':'32',
        'yellow':'33',
        'cyan':'36',
        'purple':'35',
        'blue':'34',
        'white':'37'
    }
    _style={
        'bold':'1',
        'normal':'0',
        'italic':'2'
    }
    _change='\033['+str(_style[style.lower()])+';'+str(_colorDirectory[color.lower()])+';'+str(int(_colorDirectory[bg.lower()])+10)+'m'
    _restore='\033['+str(_style['normal'])+';'+str(_colorDirectory['white'])+';'+str(int(30+10))+'m'
    try:
        return _change+str(text)+_restore
    except:
        return text
        
if __name__=='__main__':
    print(set('black','black',bg='red'))
    print(set('red   ','red'))
    print(set('green ','green'))
    print(set('yellow','yellow'))
    print(set('blue  ','blue'))
    print(set('purple','purple'))
    print(set('cyan ','cyan'))
    print(set('white','white'))
