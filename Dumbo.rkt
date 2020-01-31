;Xpilot-AI Team 2020
;Run: racket Dumbo.rkt
#lang racket
(require "rktAI.rkt")

(define mainLoop
  	(lambda () 
    		;Release keys
  		(thrust 0)
  		(turnLeft 0)
  		(turnRight 0)
  		;Set variables
		(let*  ((heading (inexact->exact (round (selfHeadingDeg))))
		   	(tracking (inexact->exact (round (selfTrackingDeg))))
  			(frontWall (wallFeeler 500 heading))
  			(leftWall (wallFeeler 500 (+ heading 5)))
  			(rightWall (wallFeeler 500 (- heading 5)))
  			(trackWall (wallFeeler 500 tracking)))
  			;Thrust rules
  			(if (and (<= (selfSpeed) 50) (>= frontWall 5))
    		   		(thrust 1)
			;else
				(when (< trackWall 5)
    		   			(thrust 1)))
  			;Turn rules
  			(if (< leftWall rightWall)
    		  		(turnRight 1)
  			;else
    				(turnLeft 1))
  			;Just keep shooting
  			(fireShot)
		)
	)
)


(start mainLoop '("-name" "Dumbo"))