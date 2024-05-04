alt_lessons = [
	[
		[
			{
				'lesson_id' : 1,
				'title' : "What is blackjack and how does a player win or lose?",
				'text' : ["The object of blackjack is to beat the dealer", "", ""],
				'spotlight' : 2,
				'next_screen' : [0, 0, 1],
				'media_array' : [('/../static/assets/images/7Diamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/KClub.png', '/../static/assets/images/10Heart.png')],
				'start_time' : 0,
				"animation" : ['Deal'],
				"interaction" : "N",
			},
   			{
				'lesson_id' : 1,
				'title' : "What is blackjack and how does a player win or lose?",
				'text' : ["", "", "The player wants to get as close to 21 as possible without going over"],
				'spotlight' : 3,
				'next_screen' : [0, 0, 2],
				'media_array' : [('/../static/assets/images/7Diamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/KClub.png', '/../static/assets/images/10Heart.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
    			"interaction" : "N",
			},	
   			{
				'lesson_id' : 1,
				'title' : "What is blackjack and how does a player win or lose?",
				'text' : ["When the dealer has a 17 or more, they can't draw another card", "", ""],
				'spotlight' : 2,
				'next_screen' : [0, 0, 3],
				'media_array' : [('/../static/assets/images/7Diamond.png', '/../static/assets/images/JDiamond.png'), ('/../static/assets/images/10Club.png', '/../static/assets/images/10Heart.png')],
				'start_time' : 0,
				"animation" : ['Reveal'],
    			"interaction" : "N",
			},
			{
				'lesson_id' : 1,
				'title' : "What is blackjack and how does a player win or lose?",
				'text' : ["", "", "You have 20 so you win!"],
				'spotlight' : 3,
				'next_screen' : [0, 1, 0],
				'media_array' : [('/../static/assets/images/7Diamond.png', '/../static/assets/images/JDiamond.png'), ('/../static/assets/images/10Club.png', '/../static/assets/images/10Heart.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction" : "N",
			},
		],
		[
			{
				'lesson_id' : 2,
				'title' : "What do the cards mean?",
				'text' : ["", "Let's learn the value of the cards.", ""],
				'spotlight' : 0,
				'next_screen' : [0, 1, 1],
				'media_array' : [('/../static/assets/images/10Diamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/7Heart.png', '/../static/assets/images/AClub.png')],
				'start_time' : 0,
				"animation" : ['Discard', 'Deal'],
				"interaction" : "N",
			},
			{
				'lesson_id' : 2,
				'title' : "What do the cards mean?",
				'text' : ["Numbers add their face value. 10 of Diamonds is 10 points.", "", ""],
				'spotlight' : 0,
				'next_screen' : [0, 1, 2],
				'media_array' : [('/../static/assets/images/10Diamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/7Heart.png', '/../static/assets/images/AClub.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
    			"interaction" : "N",
			},
      		{
				'lesson_id' : 2,
				'title' : "What do the cards mean?",
				'text' : ["", "Aces are worth 1 or 11.", "The player's hand is 8 OR an 18"],
				'spotlight' : 0,
				'next_screen' : [0, 1, 3],
				'media_array' : [('/../static/assets/images/10Diamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/7Heart.png', '/../static/assets/images/AClub.png')],
				'start_time' : 0,
				'animation' : ['Nothing'],
   				"interaction" : "N",
			},
			{
				'lesson_id' : 2,
				'title' : "What do the cards mean?",
				'text' : ["", "Here, the player has a soft hand.", "It is called a SOFT hand because you can choose the hand's value of 8 or 18"],
				'spotlight' : 3,
				'next_screen' : [0, 1, 4],
				'media_array' : [('/../static/assets/images/10Diamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/7Heart.png', '/../static/assets/images/AClub.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interacction" : "N",
			},
			{
				'lesson_id' : 2,
				'title' : "What do the cards mean?",
				'text' : ["", "Asking for another card is called hitting.", "Press H to hit!"],
				'spotlight' : 0,
				'next_screen' : [0, 1, 5],
				'media_array' : [('/../static/assets/images/10Diamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/7Diamond.png', '/../static/assets/images/KSpade.png')],
				'start_time' : 0,
				"animation" : ['Hit'],
				"interaction" : "H",
			},
			{
				'lesson_id' : 2,
				'title' : "What do the cards mean?",
				'text' : ["", "Face cards are all worth 10.", "Now, we have 1 + 7 + 10 = 18."],
				'spotlight' : 0,
				'next_screen' : [0, 1, 6],
				'media_array' : [('/../static/assets/images/10Diamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/7Diamond.png', '/../static/assets/images/KSpade.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
   				"interaction" : "N",
			},
			{
				'lesson_id' : 2,
				'title' : "What do the cards mean?",
				'text' : ["", "The player now has a HARD hand.", "Ace can only be worth 1 since 11 would push the total over 21."],
				'spotlight' : 0,
				'next_screen' : [0, 1, 7],
				'media_array' : [('/../static/assets/images/10Diamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/7Diamond.png', '/../static/assets/images/KSpade.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"intraction" : "N",
			},
			{
				'lesson_id' : 2,
				'title' : "What do the cards mean?",
				'text' : ["The dealer reveals a score of 10 + 10 = 20.", "Sorry, you lose!", "You have 18."],
				'spotlight' : 0,
				'next_screen' : [0, 2, 0],
				'media_array' : [('/../static/assets/images/10Diamond.png', '/../static/assets/images/QSpade.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/7Diamond.png', '/../static/assets/images/KSpade.png')],
				'start_time' : 0,
				"animation" : ['Reveal'],
				"intraction" : "N",
			},
		],
		[
			{
				'lesson_id' : 3,
				'title' : "Let's play a guided game!",
				'text' : ["", "Let's play a game! We'll tell you what to do.", ""],
				'spotlight' : 0,
				'next_screen' : [0, 2, 1],
				'media_array' : [('/../static/assets/images/4Club.png', '/../static/assets/images/back.png'), ('/../static/assets/images/9Spade.png', '/../static/assets/images/2Heart.png')],
				'start_time' : 0,
				"animation" : ['Discard', 'Deal'],
				"interaction" : "N",
			},
			{
				'lesson_id' : 3,
				'title' : "Let's play a guided game!",
				'text' : ["The dealer always starts with a card face down", "", ""],
				'spotlight' : 2,
				'next_screen' : [0, 2, 2],
				'media_array' : [('/../static/assets/images/4Club.png', '/../static/assets/images/back.png'), ('/../static/assets/images/9Spade.png', '/../static/assets/images/2Heart.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction" : "N",
			},
			{
				'lesson_id' : 3,
				'title' : "Let's play a guided game!",
				'text' : ["", "", "You have 11."],
				'spotlight' : 3,
				'next_screen' : [0, 2, 3],
				'media_array' : [('/../static/assets/images/4Club.png', '/../static/assets/images/back.png'), ('/../static/assets/images/9Spade.png', '/../static/assets/images/2Heart.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction" : "N",
			},
			{
				'lesson_id' : 3,
				'title' : "Let's play a guided game!",
				'text' : ["", "You should always draw a card on 11 or less because you can't go over 21.", "Let's hit!"],
				'spotlight' : 3,
				'next_screen' : [0, 2, 4],
				'media_array' : [('/../static/assets/images/4Club.png', '/../static/assets/images/back.png'), ('/../static/assets/images/9Spade.png', '/../static/assets/images/2Heart.png', '/../static/assets/images/9Spade.png')],
				'start_time' : 0,
				"animation" : ['Hit'],
				"interaction" : "H",
			},
			{
				'lesson_id' : 3,
				'title' : "Let's play a guided game!",
				'text' : ["", "Your new card gives you a total of 20. It would be hard to get 21 from here, so you want to Stand", ""],
				'spotlight' : 3,
				'next_screen' : [0, 2, 5],
				'media_array' : [('/../static/assets/images/4Club.png', '/../static/assets/images/back.png'), ('/../static/assets/images/9Spade.png', '/../static/assets/images/2Heart.png', '/../static/assets/images/9Spade.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction" : "N",
			},
			{
				'lesson_id' : 3,
				'title' : "Let's play a guided game!",
				'text' : ["", "Standing means you're done and it's the next player's turn.", "Press S to stand!"],
				'spotlight' : 3,
				'next_screen' : [0, 2, 6],
				'media_array' : [('/../static/assets/images/4Club.png', '/../static/assets/images/back.png'), ('/../static/assets/images/9Spade.png', '/../static/assets/images/2Heart.png', '/../static/assets/images/9Spade.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction" : "S",
			},
			{
				'lesson_id' : 3,
				'title' : "Let's play a guided game!",
				'text' : ["The dealer reveals a 10.", "Since you chose to stand, it is now the dealer's turn", ""],
				'spotlight' : 3,
				'next_screen' : [0, 2, 7],
				'media_array' : [('/../static/assets/images/4Club.png', '/../static/assets/images/10Diamond.png'), ('/../static/assets/images/9Spade.png', '/../static/assets/images/2Heart.png', '/../static/assets/images/9Spade.png')],
				'start_time' : 0,
				"animation" : ['Reveal'],
				"interaction" : "N",
			},
			{
				'lesson_id' : 3,
				'title' : "Let's play a guided game!",
				'text' : ["", "The dealer is required to hit when their hand is under 17.", ""],
				'spotlight' : 2,
				'next_screen' : [0, 2, 8],
				'media_array' : [('/../static/assets/images/4Club.png', '/../static/assets/images/10Diamond.png', '/../static/assets/images/JHeart.png'), ('/../static/assets/images/9Spade.png', '/../static/assets/images/2Heart.png', '/../static/assets/images/9Spade.png')],
				'start_time' : 0,
				"animation" : ['DealerHit'],
				"interaction" : "N",
			},
			{
				'lesson_id' : 3,
				'title' : "Let's play a guided game!",
				'text' : ["They draw another 10 for a total of 24. Since they have more than 21 they Bust!", "", ""],
				'spotlight' : 2,
				'next_screen' : [0, 2, 9],
				'media_array' : [('/../static/assets/images/4Club.png', '/../static/assets/images/10Diamond.png', '/../static/assets/images/JHeart.png'), ('/../static/assets/images/9Spade.png', '/../static/assets/images/2Heart.png', '/../static/assets/images/9Spade.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction" : "N",
			},
			{
				'lesson_id' : 3,
				'title' : "Let's play a guided game!",
				'text' : ["", "Busting means your hand is more than 21, and you lose.", "Player wins!"],
				'spotlight' : 2,
				'next_screen' : [0, 3, 0],
				'media_array' : [('/../static/assets/images/4Club.png', '/../static/assets/images/10Diamond.png', '/../static/assets/images/JHeart.png'), ('/../static/assets/images/9Spade.png', '/../static/assets/images/2Heart.png', '/../static/assets/images/9Spade.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction" : "N",
			},
		],
		[
			{
				'lesson_id' : 4,
				'title' : "Splitting...what is it? ",
				'text' : ["", "There are a few more terms you should know. The first is called Splitting.", ""],
				'spotlight' : 0,
				'next_screen' : [0, 3, 1],
				'media_array' : [('/../static/assets/images/JDiamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/AHeart.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction" : "N",
			},
			{
				'lesson_id' : 4,
				'title' : "Splitting...what is it? ",
				'text' : ["", "Being dealt two of the same denomination allows you to Split.", "Press T to split!"],
				'spotlight' : 3,
				'next_screen' : [0, 3, 2],
				'media_array' : [('/../static/assets/images/JDiamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/AHeart.png')],
				'start_time' : 0,
				"animation" : ['Split'],
				"interaction" : "T",
			},
			{
				'lesson_id' : 4,
				'title' : "Splitting...what is it? ",
				'text' : ["", "Splitting allows you to split your hand into two hands.", ""],
				'spotlight' : 3,
				'next_screen' : [0, 3, 3],
				'media_array' : [('/../static/assets/images/JDiamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/AHeart.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction" : "N",
			},
			{
				'lesson_id' : 4,
				'title' : "Splitting...what is it? ",
				'text' : ["", "The dealer will give you a new card for each hand and you can choose to stay or hit for each.", ""],
				'spotlight' : 3,
				'next_screen' : [0, 3, 4],
				'media_array' : [('/../static/assets/images/JDiamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/2Heart.png', '/../static/assets/images/AHeart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction" : "N",
			},
			{
				'lesson_id' : 4,
				'title' : "Splitting...what is it? ",
				'text' : ["", "You have 21 for both hands and the dealer has 17 so you win twice!", ""],
				'spotlight' : 3,
				'next_screen' : [0, 4, 0],
				'media_array' : [('/../static/assets/images/JDiamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/2Heart.png', '/../static/assets/images/AHeart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction" : "N",
			},
		],
		[
			{
				'lesson_id' : 5,
				'title' : "Learn how to Double",
				'text' : ["", "Next you'll learn how to Double", ""],
				'spotlight' : 0,
				'next_screen' : [0, 4, 1],
				'media_array' : [('/../static/assets/images/4Club.png', '/../static/assets/images/back.png'), ('/../static/assets/images/9Spade.png', '/../static/assets/images/2Heart.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction" : "N",
			},
			{
				'lesson_id' : 5,
				'title' : "Learn how to Double",
				'text' : ["", "Before you've hit on a new hand, you're allowed to Double instead.", "Press D to double!"],
				'spotlight' : 3,
				'next_screen' : [0, 4, 2],
				'media_array' : [('/../static/assets/images/4Club.png', '/../static/assets/images/back.png'), ('/../static/assets/images/9Spade.png', '/../static/assets/images/2Heart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Double'],
				"interaction" : "D",
			},
			{
				'lesson_id' : 5,
				'title' : "Learn how to Double",
				'text' : ["", "The dealer will deal you one card sideways and you can't hit again.", ""],
				'spotlight' : 3,
				'next_screen' : [0, 4, 3],
				'media_array' : [('/../static/assets/images/4Club.png', '/../static/assets/images/back.png'), ('/../static/assets/images/9Spade.png', '/../static/assets/images/2Heart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction" : "N",
			},
			{
				'lesson_id' : 5,
				'title' : "Learn how to Double",
				'text' : ["", "If your hand is larger than the dealer's or the dealer busts, you win double your bet!", ""],
				'spotlight' : 3,
				'next_screen' : [0, 4, 4],
				'media_array' : [('/../static/assets/images/4Club.png', '/../static/assets/images/KHeart.png'), ('/../static/assets/images/9Spade.png', '/../static/assets/images/2Heart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Reveal'],
				"interaction" : "N",
			},
            {
				'lesson_id' : 5,
				'title' : "Learn how to Double",
				'text' : ["", "Dealer busts. You win double!", ""],
				'spotlight' : 3,
				'next_screen' : [0, 5, 0],
				'media_array' : [('/../static/assets/images/4Club.png', '/../static/assets/images/KHeart.png', '/../static/assets/images/10Diamond.png'), ('/../static/assets/images/9Spade.png', '/../static/assets/images/2Heart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Reveal'],
				"interaction" : "N",
			},
		],
		[
			{
				'lesson_id' : 6,
				'title' : "Let's learn about Insurance!",
				'text' : ["", "The last thing you need to know is Insurance.", ""],
				'spotlight' : 0,
				'next_screen' : [0, 5, 1],
				'media_array' : [('/../static/assets/images/AClub.png', '/../static/assets/images/back.png'), ('/../static/assets/images/JDiamond.png', '/../static/assets/images/4Club.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
			},
			{
				'lesson_id' : 6,
				'title' : "Let's learn about Insurance!",
				'text' : ["If the dealer shows an ace, you'll be offered Insurance. Don't Take It. EVER!", "", ""],
				'spotlight' : 3,
				'next_screen' : [0, 5, 2],
				'media_array' : [('/../static/assets/images/AClub.png', '/../static/assets/images/back.png'), ('/../static/assets/images/JDiamond.png', '/../static/assets/images/4Club.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
			},
			{
				'lesson_id' : 6,
				'title' : "Let's learn about Insurance! ",
				'text' : ["", "Insurance is a house advantage. If you take it and they have 21, you won't lose your bet. But it's never worth it.", ""],
				'spotlight' : 3,
				'next_screen' : [0, 5, 3],
				'media_array' : [('/../static/assets/images/AClub.png', '/../static/assets/images/back.png'), ('/../static/assets/images/JDiamond.png', '/../static/assets/images/4Club.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
			},
			{
				'lesson_id' : 6,
				'title' : "Let's learn about Insurance! ",
				'text' : ["", "Instead, let's make our next move.", "Press a button to continue!"],
				'spotlight' : 3,
				'next_screen' : [0, 5, 4],
				'media_array' : [('/../static/assets/images/AClub.png', '/../static/assets/images/back.png'), ('/../static/assets/images/JDiamond.png', '/../static/assets/images/4Club.png', '/../static/assets/images/10Heart.png')],
				'start_time' : 0,
				"animation" : ['Hit'],
				"interaction" : "H",
			},
			{
				'lesson_id' : 6,
				'title' : "Let's learn about Insurance! ",
				'text' : ["", "You win! Good thing you didn't take insurance.", ""],
				'spotlight' : 3,
				'next_screen' : [1, 0, 0],
				'media_array' : [('/../static/assets/images/AClub.png', '/../static/assets/images/8Heart.png'), ('/../static/assets/images/JDiamond.png', '/../static/assets/images/4Club.png', '/../static/assets/images/7Heart.png')],
				'start_time' : 0,
				"animation" : ['Reveal'],
				"interaction" : "N",
			},
		],
	],
	[
		[
			{
				'lesson_id' : 1,
				'title' : "title needed",
				'text' : ["", "In this module you'll learn how to play 'basic strategy', It is a set of rules that gives you the best possible odds.", ""],
				'spotlight' : 0,
				'next_screen' : [1, 0, 1],
				'media_array' : [('/../static/assets/images/AClub.png', '/../static/assets/images/back.png'), ('/../static/assets/images/2Heart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Deal'],
				"interaction": "N",
			},
			{
				'lesson_id' : 1,
				'title' : "title needed",
				'text' : ["Most moves you make depend entirely on the dealer's 'upcard'. Here we see it is a 4.", "", ""],
				'spotlight' : 2,
				'next_screen' : [1, 0, 2],
				'media_array' : [('/../static/assets/images/AClub.png', '/../static/assets/images/back.png'), ('/../static/assets/images/2Heart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction": "N",
			},
			{
				'lesson_id' : 1,
				'title' : "title needed",
				'text' : ["", "", "You have a 12."],
				'spotlight' : 3,
				'next_screen' : [1, 0, 3],
				'media_array' : [('/../static/assets/images/AClub.png', '/../static/assets/images/back.png'), ('/../static/assets/images/2Heart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction": "N",
			},
			{
				'lesson_id' : 1,
				'title' : "title needed",
				'text' : ["", "What do you think we should do here? Press a button to guess!", ""],
				'spotlight' : 3,
				'next_screen' : [1, 0, 3],
				'media_array' : [('/../static/assets/images/AClub.png', '/../static/assets/images/back.png'), ('/../static/assets/images/2Heart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction": "S",
			},
			{
				'lesson_id' : 1,
				'title' : "title needed",
				'text' : ["There are more 10's than any other value card. Always assume the dealer's hidden card is a ten and the next card dealt will be a 10.", "Stand is the correct answer!", ""],
				'spotlight' : 0,
				'next_screen' : [1, 0, 4],
				'media_array' : [('/../static/assets/images/AClub.png', '/../static/assets/images/back.png'), ('/../static/assets/images/2Heart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction": "N",
			},
			{
				'lesson_id' : 1,
				'title' : "title needed",
				'text' : ["And it is!", "", ""],
				'spotlight' : 0,
				'next_screen' : [1, 0, 5],
				'media_array' : [('/../static/assets/images/AClub.png', '/../static/assets/images/JDiamond.png'), ('/../static/assets/images/2Heart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Reveal'],
				"interaction": "N",
			},
			{
				'lesson_id' : 1,
				'title' : "title needed",
				'text' : "And it is again! Dealer busts!",
				'spotlight' : 2,
				'next_screen' : [1, 0, 6],
				'media_array' : [('/../static/assets/images/AClub.png', '/../static/assets/images/JDiamond.png', '/../static/assets/images/QHeart.png'), ('/../static/assets/images/2Heart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['DealerHit'],
				"interaction": "N",
			},
			{
				'lesson_id' : 1,
				'title' : "title needed",
				'text' : ["", "", "If your hand was a 13, 14, 15 etc…the result would be the same"],
				'spotlight' : 3,
				'next_screen' : [1, 0, 7],
				'media_array' : [('/../static/assets/images/AClub.png', '/../static/assets/images/JDiamond.png', '/../static/assets/images/QHeart.png'), ('/../static/assets/images/2Heart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"intraction" : "N",
			},
			{
				'lesson_id' : 1,
				'title' : "title needed",
				'text' : ["So if the dealer's upcard is a 2-6, always stand on 12+", "", "Remember, still hit on 11 or less because you can't bust!"],
				'spotlight' : 0,
				'next_screen' : [1, 1, 0],
				'media_array' : [('/../static/assets/images/AClub.png', '/../static/assets/images/JDiamond.png', '/../static/assets/images/QHeart.png'), ('/../static/assets/images/2Heart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction": "N",
			},
		],
		[
			{
				'lesson_id' : 2,
				'title' : "title needed",
				'text' : ["", "Let's consider another scenario…", ""],
				'spotlight' : 0,
				'next_screen' : [1, 1, 1],
				'media_array' : [('/../static/assets/images/7Diamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/6Heart.png')],
				'start_time' : 0,
				"animation" : ['Discard', 'Deal'],
				"interaction": "N",
			},
			{
				'lesson_id' : 2,
				'title' : "title needed",
				'text' : ["Now the dealer is showing a 7. We assume his hidden card is a 10.", "", ""],
				'spotlight' : 2,
				'next_screen' : [1, 1, 2],
				'media_array' : [('/../static/assets/images/7Diamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/6Heart.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction": "N",
			},
			{
				'lesson_id' : 2,
				'title' : "title needed",
				'text' : ["", "What should we do? Press a button to try!", "You have a 16. You'll lose if the dealer has a 10."],
				'spotlight' : 3,
				'next_screen' : [1, 1, 3],
				'media_array' : [('/../static/assets/images/7Diamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/6Heart.png', '/../static/assets/images/4Club.png')],
				'start_time' : 0,
				"animation" : ['Hit'],
				"interaction": "H",
			},
			{
				'lesson_id' : 2,
				'title' : "title needed",
				'text' : ["", "Hit was correct!", "You draw a 4."],
				'spotlight' : 3,
				'next_screen' : [1, 1, 4],
				'media_array' : [('/../static/assets/images/7Diamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/6Heart.png', '/../static/assets/images/4Club.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction": "N",
			},
			{
				'lesson_id' : 2,
				'title' : "title needed",
				'text' : ["", "So if the dealer's upcard is 7-A, always hit when you have 16 or less.", "You win!"],
				'spotlight' : 0,
				'next_screen' : [1, 2, 0],
				'media_array' : [('/../static/assets/images/7Diamond.png', '/../static/assets/images/JClub.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/6Heart.png', '/../static/assets/images/4Club.png')],
				'start_time' : 0,
				'animation' : ['Reveal'],
				"interaction": "N",
			},
		],
		[
			{
				'lesson_id' : 3,
				'title' : "title needed",
				'text' : ["", "Let's consider soft hands.", "Remember, a soft hand is a hand with an Ace that can be counted as 1 or 11."],
				'spotlight' : 3,
				'next_screen' : [1, 2, 1],
				'media_array' : [('/../static/assets/images/7Heart.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/6Heart.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction": "N",
			},
			{
				'lesson_id' : 3,
				'title' : "title needed",
				'text' : ["", "", "Total: 7 or 17"],
				'spotlight' : 3,
				'next_screen' : [1, 2, 2],
				'media_array' : [('/../static/assets/images/7Heart.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/6Heart.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction": "N",
			},
			{
				'lesson_id' : 3,
				'title' : "title needed",
				'text' : ["", "We assume the next card is a 10. Then, after we hit, our HARD hand will become the same as the higher value of our SOFT hand.", "Let's hit!"],
				'spotlight' : 3,
				'next_screen' : [1, 2, 3],
				'media_array' : [('/../static/assets/images/7Heart.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/6Heart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Hit'],
				"interaction": "H",
			},
			{
				'lesson_id' : 3,
				'title' : "title needed",
				'text' : ["", "", "Total: Hard 17."],
				'spotlight' : 3,
				'next_screen' : [1, 2, 4],
				'media_array' : [('/../static/assets/images/7Heart.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/6Heart.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction": "N",
			},
			{
				'lesson_id' : 3,
				'title' : "title needed",
				'text' : ["", "However, there is a also a chance you could pull a smaller card…", ""],
				'spotlight' : 3,
				'next_screen' : [1, 2, 5],
				'media_array' : [('/../static/assets/images/7Heart.png', '/../static/assets/images/back.png'), ('/../static/assets/images/6Heart.png', '/../static/assets/images/AClub.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction": "N",
			},
   			{
				'lesson_id' : 3,
				'title' : "title needed",
				'text' : ["", "Try hitting again!", ""],
				'spotlight' : 3,
				'next_screen' : [1, 2, 6],
				'media_array' : [('/../static/assets/images/7Heart.png', '/../static/assets/images/back.png'), ('/../static/assets/images/6Heart.png', '/../static/assets/images/AClub.png', '/../static/assets/images/4Diamond.png')],
				'start_time' : 0,
				"animation" : ['Hit'],
				"interaction": "H",
			},
			{
				'lesson_id' : 3,
				'title' : "title needed",
				'text' : ["", "Wow, nice!", "This soft hand could be 11 or 21."],
				'spotlight' : 3,
				'next_screen' : [1, 2, 7],
				'media_array' : [('/../static/assets/images/7Heart.png', '/../static/assets/images/back.png'), ('/../static/assets/images/6Heart.png', '/../static/assets/images/AClub.png', '/../static/assets/images/4Diamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction": "N",
			},
			{
				'lesson_id' : 3,
				'title' : "title needed",
				'text' : ["", "So always hit on soft hands that have a high total of 17 or less.", ""],
				'spotlight' : 3,
				'next_screen' : [1, 3, 0],
				'media_array' : [('/../static/assets/images/7Heart.png', '/../static/assets/images/back.png'), ('/../static/assets/images/6Heart.png', '/../static/assets/images/AClub.png', '/../static/assets/images/4Diamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction": "N",
			},
		],
		[
			{
				'lesson_id' : 4,
				'title' : "title needed",
				'text' : ["", "What if you have a soft hand of 18 or higher?", "Make a move to find out!"],
				'spotlight' : 3,
				'next_screen' : [1, 3, 1],
				'media_array' : [('/../static/assets/images/7Heart.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/7Diamond.png')],
				'start_time' : 0,
				"animation" : ['Discard', 'Deal'],
				"interaction": "S",
			},
			{
				'lesson_id' : 4,
				'title' : "title needed",
				'text' : ["", "It's best to stand on any soft hand with a high total above 18.", ""],
				'spotlight' : 3,
				'next_screen' : [1, 3, 2],
				'media_array' : [('/../static/assets/images/7Heart.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/7Diamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction": "N",
			},
			{
				'lesson_id' : 4,
				'title' : "title needed",
				'text' : ["Dealer has 17.", "You win!", ""],
				'spotlight' : 0,
				'next_screen' : [1, 4, 0],
				'media_array' : [('/../static/assets/images/7Heart.png', '/../static/assets/images/10Club.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/7Diamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
				"interaction": "N",
			},
		],
		[
			{
				'lesson_id' : 5,
				'title' : "title needed",
				'text' : ["", "Let's talk about when to split.", ""],
				'spotlight' : 0,
				'next_screen' : [1, 4, 1],
				'media_array' : [('/../static/assets/images/JDiamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/AHeart.png')],
				'start_time' : 0,
				"animation" : ['Discard', 'Deal'],
			},
			{
				'lesson_id' : 5,
				'title' : "title needed",
				'text' : ["", "", "Do you recall what to do with two aces? Press a button to guess!"],
				'spotlight' : 3,
				'next_screen' : [1, 4, 2],
				'media_array' : [('/../static/assets/images/JDiamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/AHeart.png')],
				'start_time' : 0,
				"animation" : ['Split'],
				"interaction": "T",
			},
			{
				'lesson_id' : 5,
				'title' : "title needed",
				'text' : ["", "Exactly Right! ALWAYS split aces on any hand.", "Let's hit for both Aces!"],
				'spotlight' : 3,
				'next_screen' : [1, 4, 3],
				'media_array' : [('/../static/assets/images/JDiamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/JHeart.png', '/../static/assets/images/AHeart.png', '/../static/assets/images/10Diamond.png')],
				'start_time' : 0,
				"animation" : ['HitSplit'],
				"interaction": "H",
			},
   			{
				'lesson_id' : 5,
				'title' : "title needed",
				'text' : ["The dealer only had 18!", "You won, and now you win double your bet!", ""],
				'spotlight' : 3,
				'next_screen' : [1, 4, 3],
				'media_array' : [('/../static/assets/images/JDiamond.png', '/../static/assets/images/8Heart.png'), ('/../static/assets/images/AClub.png', '/../static/assets/images/JHeart.png', '/../static/assets/images/AHeart.png', '/../static/assets/images/10Diamond.png')],
				'start_time' : 0,
				"animation" : ['Reveal'],
			},
			{
				'lesson_id' : 5,
				'title' : "title needed",
				'text' : ["", "Should you always split eights too?", "Press a button to guess!"],
				'spotlight' : 3,
				'next_screen' : [1, 4, 4],
				'media_array' : [('/../static/assets/images/10Club.png', '/../static/assets/images/back.png'), ('/../static/assets/images/8Diamond.png', '/../static/assets/images/8Club.png')],
				'start_time' : 0,
				"animation" : ['Discard', 'Deal', 'Split'],
				"interaction": "T",
			},
			{
				'lesson_id' : 5,
				'title' : "title needed",
				'text' : ["", "Yes! 16 (8+8) is the worst total you can have. Splitting gives you a chance to change your luck!", "Now, let's hit for both eights!"],
				'spotlight' : 3,
				'next_screen' : [1, 4, 5],
				'media_array' : [('/../static/assets/images/10Club.png', '/../static/assets/images/back.png'), ('/../static/assets/images/8Diamond.png', '/../static/assets/images/10Heart.png', '/../static/assets/images/8Club.png', '/../static/assets/images/QDiamond.png')],
				'start_time' : 0,
				"animation" : ['HitSplit'],
				"interaction": "H",
			},
			{
				'lesson_id' : 5,
				'title' : "title needed",
				'text' : ["The dealer only had 17. Nice win!", "So, always split As and 8s!"],
				'spotlight' : 0,
				'next_screen' : [1, 5, 0],
				'media_array' : [('/../static/assets/images/10Club.png', '/../static/assets/images/7Heart.png'), ('/../static/assets/images/8Diamond.png', '/../static/assets/images/10Heart.png', '/../static/assets/images/8Club.png', '/../static/assets/images/QDiamond.png')],
				'start_time' : 0,
				"animation" : ['Reveal'],
				"intraction" : "N",
			},
		],
		[
			{
				'lesson_id' : 6,
				'title' : "title needed",
				'text' : "The last thing you need to know is when to double",
				'spotlight' : 0,
				'next_screen' : [1, 5, 1],
				'media_array' : [('/../static/assets/images/back.png', '/../static/assets/images/back.png'), ('/../static/assets/images/back.png', '/../static/assets/images/back.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
			},
			{
				'lesson_id' : 6,
				'title' : "title needed",
				'text' : "11 is the best starting hand outside of blackjack (21)",
				'spotlight' : 3,
				'next_screen' : [1, 5, 2],
				'media_array' : [('/../static/assets/images/JDiamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/8Heart.png', '/../static/assets/images/3Diamond.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
			},
			{
				'lesson_id' : 6,
				'title' : "title needed",
				'text' : "21! Blackjack! We doubled our bet!",
				'spotlight' : 3,
				'next_screen' : [1, 5, 3],
				'media_array' : [('/../static/assets/images/JDiamond.png', '/../static/assets/images/back.png'), ('/../static/assets/images/8Heart.png', '/../static/assets/images/3Diamond.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
			},
			{
				'lesson_id' : 6,
				'title' : "title needed",
				'text' : "10 should always be doubled UNLESS the dealer shows a 10 or an 8",
				'spotlight' : 3,
				'next_screen' : [1, 5, 4],
				'media_array' : [('/../static/assets/images/8Heart.png', '/../static/assets/images/back.png'), ('/../static/assets/images/3Diamond.png', '/../static/assets/images/7Diamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
			},
			{
				'lesson_id' : 6,
				'title' : "title needed",
				'text' : "20! We bet again. Double our bet!",
				'spotlight' : 3,
				'next_screen' : [2, 0, 0],
				'media_array' : [('/../static/assets/images/8Heart.png', '/../static/assets/images/JDiamond.png'), ('/../static/assets/images/7Diamond.png', '/../static/assets/images/3Diamond.png', '/../static/assets/images/JDiamond.png')],
				'start_time' : 0,
				"animation" : ['Nothing'],
			},
		],
	],
]
