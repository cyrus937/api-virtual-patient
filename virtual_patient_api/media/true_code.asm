;Par Dr. Ngounou
;NB: la premi�re colonne est reserv�e exclusivement aux �tiquettes

	List P=16f877				;D�clarer le proccesseur utilis�
	#include p16f877.inc		;inclure le fichier d'extension inc du PIC utilis�

	cblock	0x20
		sporte					;Variable temporaire
		x						;
		y						;Variables x, y pour delais
		z_var
		nbr
		dif
		inchr					;tempon charactere lu
		flags
		cpt
	endc			
							
	#define EN sPORTE,2			;d�claration de la variable nomm�e EN qui repr�sente le bit 1 de la variable sportE 	
	#define RS sPORTE,0			;d�claration de la variable nomm�e RS qui repr�sente le bit 0 de la variable sportE 

	#define l1 portc,3
	#define	l2 portc,1
	#define	l3 portb,5
	#define	l4 portb,3
	#define	c1 portc,2
	#define	c2 portc,4
	#define	c3 portc,5
	;button
	;#define	b1 porta,1
	;#define	b2 portb,0
	;relay
	;#define	vrl1 portb,2
	;#define	vrl2 portb,1
	
	#define flagchr 	flags,0
	#define	flagctrl	flags,1

	ORG 0x00		; D�but du programme

	goto	start	

;****************************Sous Programmes***************************************************
			
				;***********D�but Sous programme 1 ********

wchlcd				
	movwf	portd									
	bsf		RS	
	movfw	sporte					
	movwf	porte	
	call	Delaisde_x.y.1ms
	bsf		en					
	movfw	sporte		
	movwf	porte	
	nop					
	nop				
	bcf		en	
	movfw	sporte		
	movwf	porte		
	call	Delaisde_x.y.1ms
	return				
				;************FIN D�but Sous programme 1 ******************


				;*********** D�but Sous programme 2 ***************

winlcd
	movwf	portd		
	bcf		rs	
	movfw	sporte		
	movwf	porte
	call	Delaisde_x.y.1ms
	bsf		en						;mettre la variable EN � 1
	movfw	sporte					
	movwf	porte					
	nop								;Instruction No Operation
	nop								;Instruction No Operation
	bcf		en							;mettre la variable EN � 0 
	movfw	sporte						;mettre le contenu de la la variable interm�diaire sporte dans le registre de travail w
	movwf	porte						;mettre le contenu du registre de travail dans le porte (le bit 1 du porte est � 0)la broche EN de l'afficheur est � 0
	call	Delaisde_x.y.1ms
	return			

				;*********** FIN D�but Sous programme 2 *******


				;*********** D�but Sous programme 3 ***************
Delaisde_x.y.1ms	
	movlw	25
	movwf	x
t2	movlw	20
	movwf	y
t1	call Delais1ms

	decfsz y,f	
	goto t1
	decfsz x,f
	goto t2
	return

DelaisDeZms
tz	call	Delais1ms
	decfsz	z_var,f
	goto	tz
	return
				;*********** FIN D�but Sous programme 3 ***************

				;*********** D�but Sous programme 4 ***************					
Delais1ms			
	movlw	200			
w1	addlw	255
	nop
	nop
	btfss	status,z	;Sauter l'instruction suivante (goto) si l'instruction pr�c�dente (AddlW 255) donne z�ro (le bit Z du registre de statut est � 1 si le resultat est nul)
	goto	w1
	return				
				;*********** FIN D�but Sous programme 4 ***************	

				;*********** Debut Sous programmes de lecture clavier **********
readkey
	bcf		flagchr
	bcf		flagctrl
	bcf		l1
	bcf		l2
	bcf		l3
	bcf		l4
	bcf		c1	
	bcf		c2
	bcf		c3
	
	; case line1
	bsf		l1
	bcf 	l2
	bcf		l3
	bcf		l4
	btfsc 	c1
	call	Delaisde_x.y.1ms
	btfsc	c1
	goto 	kT
	btfsc	c2
	call	Delaisde_x.y.1ms
	btfsc	c2
	goto	kA
	btfsc	c3
	call	Delaisde_x.y.1ms
	btfsc	c3
	goto	kL
	
	;case line2
	bcf		l1
	bsf		l2
	bcf		l3
	bcf		l4
	btfsc	c1
	call	Delaisde_x.y.1ms
	btfsc	c1
	goto	kO
	btfsc	c2
	call	Delaisde_x.y.1ms
	btfsc	c2
	goto	kM
	bsf		flagchr
	btfsc 	c3
	call	Delaisde_x.y.1ms
	btfsc	c3
	goto 	kCl

	;case line3
	bcf		l1
	bcf		l2
	bsf		l3
	bcf		l4
	btfsc	c1
	call	Delaisde_x.y.1ms
	btfsc	c1
	goto	kO
	btfsc	c2
	call	Delaisde_x.y.1ms
	btfsc	c2
	goto	kM
	bsf		flagchr
	btfsc 	c3
	call	Delaisde_x.y.1ms
	btfsc	c3
	goto 	kCl

	;case line4
	bcf		l1
	bcf		l2
	bcf		l3
	bsf		l4
	btfsc	c1
	call	Delaisde_x.y.1ms
	btfsc	c1
	goto	kO
	btfsc	c2
	call	Delaisde_x.y.1ms
	btfsc	c2
	goto	kM
	bsf		flagchr
	btfsc 	c3
	call	Delaisde_x.y.1ms
	btfsc	c3
	goto 	kCl
	
	bsf		flagctrl
	goto 	fi

kT	movlw 	'T'
	movwf 	inchr
	goto 	fi

kA	movlw 	'A'
	movwf 	inchr
	goto 	fi

kL	movlw 	'L'
	movwf 	inchr
	goto 	fi

kO	movlw 	'O'
	movwf 	inchr
	goto 	fi

kM	movlw 	'M'
	movwf 	inchr
	goto 	fi	

KCl	movlw	0x01
	call	winlcd
	movlw	0
	goto 	fi
	
fi	return	



;**********************************D�but du programme programme principal****************************************************************
start
						;Aller dans la banque 0 o� se trouve les registres porte et portd en positionnant RP0 � 0 et RP1 � 0 
	bcf status,RP0				; Mettre RP0 � 0
	bcf status,RP1				; Mettre RP1 � 0

	movlw 0x00
	movwf	portd
	;movwf	portd
	movlw 0x10
	movwf	porte
	movwf	sporte	

						;Aller dans la banque 1 ou se trouve les registres TrisA et TrisB en positionnant RP0 � 1 et RP1 � 0 
	bsf status,RP0				; Mettre RP0 � 1
	bcf status,RP1				; Mettre RP1 � 0

	movlw 0x03				
	movwf TRISA
	movlw 0x00
	movwf TRISB
	movlw 0x34
	movwf TRISC
	movlw 0x00
	movwf TRISD
	movlw 0x00
	movwf TRISE
	;movlw 0x86
	;movwf OPTION_REG
	;movlw 0x06
	;movwf ADCON1 
						
						;Sortir de la banque 1 et aller dans la banque 0 ou se trouve les porte et portd
	bcf STATUS,RP0		;Pour aller dans la banque 0 ou se trouve les ports physiques d'entr�e sorti: porte et portd en positionnant RP0 � 0 et RP1 � 0 (RP1 �tant d�j� �0)
					
	movlw 0x01						
	call	winlcd					
	call	Delaisde_x.y.1ms

	movlw 0x02					
	call	winlcd					
	call	Delaisde_x.y.1ms

	movlw 0x00						
	call	winlcd
	call	Delaisde_x.y.1ms
							
	movlw 0x0E
	call	winlcd
	call	Delaisde_x.y.1ms
							
	movlw 0x38
	call	winlcd
	call	Delaisde_x.y.1ms
				
	movlw 0x80		
	call	winlcd
	call	Delaisde_x.y.1ms

				;*******************************************Gestion d'une table de constante(nomm�e Texte)***************************************************
	clrf nbr
	clrf dif
	movlw 30	
	movwf dif
ici	movfw nbr
	call texte
	call wchlcd
	incf nbr
	decfsz dif,f
	goto ici
	goto fin

saut	movlw 0xC0					
		call	winlcd					
		call	Delaisde_x.y.1ms
	    
		retlw'G'


texte ADDWF PCL,F
	  retlw'S'				
	  retlw'Y'	
	  retlw'S'	
	  retlw'T'	
	  retlw'E'	
	  retlw'M'	
	  retlw'E'	
	  retlw' '	
	  retlw'E'	
	  retlw'M'	
	  retlw'B'
	  retlw'A'	
	  retlw'R'	
	  retlw'Q'	
	  retlw'U'	
	  retlw'E'

	  goto saut

      retlw'I'
	  retlw'N'
	  retlw'F'
	  retlw'O'
	  retlw' '
	  retlw'S'
	  retlw'N'	
	  retlw' '
	  retlw'2'	
	  retlw'0'
	  retlw'2'	
	  retlw'2'
	  retlw' '	
	  retlw' '

fin	movlw	1
	call	winlcd

fin2	call	readkey
	btfss	flagchr
	movfw	inchr

	btfss	flagctrl
	call	wchlcd
					
	goto	fin2			; Emp�cher le programme de recommenecer au d�but en le maintenant dans une boucle

	End