;Xpilot-AI Team 2012
(module rktAI racket/base
  (provide (all-defined-out))
  (require ffi/unsafe)
  (define ai
    (ffi-lib "librktAI"))
  (define aistart ; Thanks to mithos28 for helping me pass a list -EGG
    (get-ffi-obj "start" ai (_fun _int (_list i _string) -> _int)))
  (define (start f [l '()]) ; Initialize AI interface and start XPilot -JRA
    (set-ffi-obj! "AI_loop" ai (_fun -> _void) f)
    (aistart (+ (length l) 1) (append '("xpilot-ng-x11") l)))
  (define headlessMode ;allows client to run without opening a window -CJG
    (get-ffi-obj "headlessMode" ai (_fun -> _void)))
  ; Movement methods -JNE
  (define turnLeft ; Turns left -JRA
    (get-ffi-obj "turnLeft" ai (_fun _int -> _void)))
  (define turnRight; Turns right -JRA
    (get-ffi-obj "turnRight" ai (_fun _int -> _void)))
  (define turn; Turns to an inputed Speed of Degree -JRA
    (get-ffi-obj "turn" ai (_fun _int -> _void)))
  (define turnToDeg; Turns the ship to the inputed Degree -JRA
    (get-ffi-obj "turnToDeg" ai (_fun _int -> _void)))
  (define thrust; Thrust the ship -JRA
    (get-ffi-obj "thrust" ai (_fun _int -> _void)))
  (define setTurnSpeed; Sets the speed the ship will turn by, the minimum power level is 4.0 and the maximum power is 64.0 -JRA
    (get-ffi-obj "setTurnSpeed" ai (_fun _double -> _void)))
  (define setTurnSpeedDeg; Sets the turnspeed in degrees -CJG
    (get-ffi-obj "setTurnSpeedDeg" ai (_fun _int -> _void)))
  (define setPower; Sets the speed the ship will thrust by, the minimum power level is 5.0 and the maximum power is 55.0 -JRA
    (get-ffi-obj "setPower" ai (_fun _double -> _void)))
  (define fasterTurnrate; Increases the ship's Turn Rate -JRA
    (get-ffi-obj "fasterTurnrate" ai (_fun -> _void)))
  (define slowerTurnrate; Decreases the ship's Turn Rate -JRA
    (get-ffi-obj "slowerTurnrate" ai (_fun -> _void)))
  (define morePower; Increases the ship's Thrusting Power -JRA
    (get-ffi-obj "morePower" ai (_fun -> _void)))
  (define lessPower; Decreases the ship's Thrusting Power -JRA
    (get-ffi-obj "lessPower" ai (_fun -> _void)))
  ; Shooting methods -JNE
  (define fireShot ; Fires a Shot -JRA
    (get-ffi-obj "fireShot" ai (_fun -> _void)))
  (define fireMissile; Fires a Missile -JRA
    (get-ffi-obj "fireMissile" ai (_fun -> _void)))
  (define fireTorpedo; Fires a Torpedo -JRA
    (get-ffi-obj "fireTorpedo" ai (_fun -> _void)))
  (define fireHeat; Fires a Heat Seeking Missile -JRA
    (get-ffi-obj "fireHeat" ai (_fun -> _void)))
  (define dropMine; Drops a Stationary Mine from the ship -JRA
    (get-ffi-obj "dropMine" ai (_fun -> _void)))
  (define detachMine; Releases a Mine from the ship -JRA
    (get-ffi-obj "detachMine" ai (_fun -> _void)))
  (define detonateMines; Detonates released Mines -JRA
    (get-ffi-obj "detonateMines" ai (_fun -> _void)))
  (define fireLaser; Fires a Laser -JRA
    (get-ffi-obj "fireLaser" ai (_fun -> _void)))
  ; Item usage methods -JNE
  (define tankDetach; Detaches a fuel tank from the ship -JRA
    (get-ffi-obj "tankDetach" ai (_fun -> _void)))
  (define cloak; Cloaks the ship -JRA
    (get-ffi-obj "cloak" ai (_fun -> _void)))
  (define ecm; Launches an ECM to temporarily blind opponents -JRA
    (get-ffi-obj "ecm" ai (_fun -> _void)))
  (define transporter; Uses the transporter item to steal an opponent's item or fuel -JRA
    (get-ffi-obj "transporter" ai (_fun -> _void)))
  (define tractorBeam; Uses the ship's Tractor Beam to pull in enemy ships -JRA
    (get-ffi-obj "tractorBeam" ai (_fun _int -> _void)))
  (define pressorBeam; Uses the ship's Pressor Beam to push away enemy ships -JRA
    (get-ffi-obj "pressorBeam" ai (_fun _int -> _void)))
  (define phasing; Uses the Phasing item to allow the ship to pass through walls -JRA
    (get-ffi-obj "phasing" ai (_fun -> _void)))
  (define shield; Turns on or off the ship's Shield -JRA
    (get-ffi-obj "shield" ai (_fun -> _void)))
  (define emergencyShield; Uses the Emergency Shield item to protect your ship from damage for a period of time -JRA
    (get-ffi-obj "emergencyShield" ai (_fun -> _void)))
  (define hyperjump; Uses the Hyper Jump item to warp the ship to a random location -JRA
    (get-ffi-obj "hyperjump" ai (_fun -> _void)))
  (define nextTank; Switches to the ship's next fuel tank -JRA
    (get-ffi-obj "nextTank" ai (_fun -> _void)))
  (define prevTank; Switches to the ship's previous fuel tank -JRA
    (get-ffi-obj "prevTank" ai (_fun -> _void)))
  (define toggleAutopilot; Uses the Autopilot item to stop the ship's movement -JRA
    (get-ffi-obj "toggleAutopilot" ai (_fun -> _void)))
  (define emergencyThrust; Uses the Emergency Thrust item to increase the ship's movement speed for a period of time -JRA
    (get-ffi-obj "emergencyThrust" ai (_fun -> _void)))
  (define deflector; Uses the deflector item to push everything away from the ship -JRA
    (get-ffi-obj "deflector" ai (_fun -> _void)))
  (define selectItem; Selects the ships item to be dropped -JRA
    (get-ffi-obj "selectItem" ai (_fun -> _void)))
  (define loseItem; Drops the ships selected item ; Commented out no idea why, I didn't do it -JRA
    (get-ffi-obj "loseItem" ai (_fun -> _void)))
  ; Lock methods -JNE
  (define lockNext; Locks onto the next ship in the ship buffer -JRA
    (get-ffi-obj "lockNext" ai (_fun -> _void)))
  (define lockPrev; Locks onto the prev ship in the ship buffer -JRA
    (get-ffi-obj "lockPrev" ai (_fun -> _void)))
  (define lockClose; Locks onto the closest ship -JRA
    (get-ffi-obj "lockClose" ai (_fun -> _void)))
  (define lockNextClose; Locks-on to the next closest ship -JRA
    (get-ffi-obj "lockNextClose" ai (_fun -> _void)))
  (define loadLock1; Load a saved lock-on enemy ship -JRA
    (get-ffi-obj "loadLock1" ai (_fun -> _void)))
  (define loadLock2; Load a saved lock-on enemy ship -JRA
    (get-ffi-obj "loadLock2" ai (_fun -> _void)))
  (define loadLock3; Load a saved lock-on enemy ship -JRA
    (get-ffi-obj "loadLock3" ai (_fun -> _void)))
  (define loadLock4; Load a saved lock-on enemy ship -JRA
    (get-ffi-obj "loadLock4" ai (_fun -> _void)))
  ; Modifier methods -JNE
  (define toggleNuclear; Toggles the option to have the ship fire Nuclear weapons instead of regualar weapons, takes up five mines or seven missile -JRA
    (get-ffi-obj "toggleNuclear" ai (_fun -> _void)))
  (define togglePower; Toggles the Power of the weapon -JRA
    (get-ffi-obj "togglePower" ai (_fun -> _void)))
  (define toggleVelocity; Modifies explosion velocity of mines and missiles -JRA
    (get-ffi-obj "toggleVelocity" ai (_fun -> _void)))
  (define toggleCluster; Toggles the option to have the ship fire Cluster weapons instead of regular weapons -JRA
    (get-ffi-obj "toggleCluster" ai (_fun -> _void)))
  (define toggleMini; Toggles the option to have the ship fire Mini weapons instead of regular weapons -JRA
    (get-ffi-obj "toggleMini" ai (_fun -> _void)))
  (define toggleSpread; Toggles the option to have the ship fire Spread weapons instead of regular weapons -JRA
    (get-ffi-obj "toggleSpread" ai (_fun -> _void)))
  (define toggleLaser; Toggles between the LS stun laser and the LB blinding laser -JRA
    (get-ffi-obj "toggleLaser" ai (_fun -> _void)))
  (define toggleImplosion; Toggle the option to have mines and missiles implode instead of exlode, the explosion will draw in players instead of blowing them away -JRA
    (get-ffi-obj "toggleImplosion" ai (_fun -> _void)))
  (define toggleUserName; Toggles the displayed information on the HUD on the left of the screen -JRA
    (get-ffi-obj "toggleUserName" ai (_fun -> _void)))
  (define loadModifiers1; Loads Modifiers -JRA
    (get-ffi-obj "loadModifiers1" ai (_fun -> _void)))
  (define loadModifiers2; Loads Modifiers -JRA
    (get-ffi-obj "loadModifiers2" ai (_fun -> _void)))
  (define loadModifiers3; Loads Modifiers -JRA
    (get-ffi-obj "loadModifiers3" ai (_fun -> _void)))
  (define loadModifiers4; Loads Modifiers -JRA
    (get-ffi-obj "loadModifiers4" ai (_fun -> _void)))
  (define clearModifiers; Loads Modifiers -JRA
    (get-ffi-obj "clearModifiers" ai (_fun -> _void)))
  ; map features -JNE
  (define connector; Connects the ship to the ball in Capture the Flag Mode -JRA
    (get-ffi-obj "connector" ai (_fun _int -> _void)))
  (define dropBall; Drops the ball in Capture the Flag Mode -JRA
    (get-ffi-obj "dropBall" ai (_fun -> _void)))
  (define refuel; Refuels the ship -JR
    (get-ffi-obj "refuel" ai (_fun _int -> _void)))
  ; other options -JNE
  (define keyHome; Changes the ship's Home Base or respawn location -JRA
    (get-ffi-obj "keyHome" ai (_fun -> _void)))
  (define selfDestruct; Triggers the ship's Self Destruct mechanism //Do not repeatedly press or the ship will not self destruct, it works as a toggle and has a timer -JRA
    (get-ffi-obj "selfDestruct" ai (_fun -> _void)))
  (define pauseAI; Pauses the game for the ship, does not affect other ships -JRA
    (get-ffi-obj "pauseAI" ai (_fun -> _void)))
  (define swapSettings; Swaps between ship Settings for turn rate and thrusting power -JRA 
    (get-ffi-obj "swapSettings" ai (_fun -> _void)))
  (define quitAI; Quits the game ; Do not have toggleNuclear in the same code segment or else it will not quit -JRA
    (get-ffi-obj "quitAI" ai (_fun -> _void)))
  (define talkKey; Opens up the chat window -JRA
    (get-ffi-obj "talkKey" ai (_fun -> _void)))
  (define toggleCompass; Toggles the ship's Compass -JRA
    (get-ffi-obj "toggleCompass" ai (_fun -> _void)))
  (define toggleShowMessage; Toggles Messages on the HUD on the left side of the screen -JRA 
    (get-ffi-obj "toggleShowMessage" ai (_fun -> _void)))
  (define toggleShowItems; Toggles Items on the HUD on the left side of the screen -JRA 
    (get-ffi-obj "toggleShowItems" ai (_fun -> _void)))
  (define repair; Repairs a target -JRA
    (get-ffi-obj "repair" ai (_fun -> _void)))
  (define reprogram; Reprogram a modifier or lock bank -JRA
    (get-ffi-obj "reprogram" ai (_fun -> _void)))
  (define talk; Sends a message -JRA
    (get-ffi-obj "talk" ai (_fun _string -> _void)))
  (define scanMsg; Returns the specified message -EGG
    (get-ffi-obj "scanMsg" ai (_fun _int -> _string)))
  (define scanGameMsg; Returns the specified message -EGG
    (get-ffi-obj "scanGameMsg" ai (_fun _int -> _string)))
  ; self properties -JNE
  (define selfX; Returns the ship's X Position -JRA
    (get-ffi-obj "selfX" ai (_fun -> _int)))
  (define selfY; Returns the ship's Y Position -JRA
    (get-ffi-obj "selfY" ai (_fun -> _int)))
  (define selfRadarX; Returns the ship's X Radar Coordinate -JRA
    (get-ffi-obj "selfRadarX" ai (_fun -> _int)))
  (define selfRadarY; Returns the ship's Y Radar Coordinate -JRA
    (get-ffi-obj "selfRadarY" ai (_fun -> _int)))
  (define selfVelX; Returns the ship's X Velocity -JRA
    (get-ffi-obj "selfVelX" ai (_fun -> _int)))
  (define selfVelY; Returns the ship's Y Velocity -JRA
    (get-ffi-obj "selfVelY" ai (_fun -> _int)))
  (define selfSpeed; Returns the ship's Speed -JRA
    (get-ffi-obj "selfSpeed" ai (_fun -> _int)))
  (define lockHeadingDeg; Returns in Degrees the direction of the ship's Lock-on of an enemy -JRA
    (get-ffi-obj "lockHeadingDeg" ai (_fun -> _double)))
  (define lockHeadingRad; Returns in Radians the direction of the ship's Lock-on of an enemy -JRA
    (get-ffi-obj "lockHeadingRad" ai (_fun -> _double)))
  (define selfLockDist; Returns the Distance of the enemy that the ship has Locked-on to -JRA
    (get-ffi-obj "selfLockDist" ai (_fun -> _short)))
  (define selfReload; Returns the player's Reload time remaining, based on a call to fireShot() -JRA 
    (get-ffi-obj "selfReload" ai (_fun -> _int)))
  (define selfID; Returns the ID of the ship -JRA
    (get-ffi-obj "selfID" ai (_fun -> _int)))
  (define selfAlive; Returns if the ship is Dead or Alive -JRA
    (get-ffi-obj "selfAlive" ai (_fun -> _int)))
  (define selfTeam; Returns the ship's Team -JRA
    (get-ffi-obj "selfTeam" ai (_fun -> _int)))
  (define selfLives; Returns how many Lives are left for the ship -JRA
    (get-ffi-obj "selfLives" ai (_fun -> _int)))
  (define selfTrackingRad; Returns the ship's Tracking in Radians -JRA
    (get-ffi-obj "selfTrackingRad" ai (_fun -> _double)))
  (define selfTrackingDeg; Returns the ship's Tracking in Degrees -JRA
    (get-ffi-obj "selfTrackingDeg" ai (_fun -> _double)))
  (define selfHeadingDeg; Returns the Direction of the ship's Lock-on from the ship in Degrees -JRA
    (get-ffi-obj "selfHeadingDeg" ai (_fun -> _double)))
  (define selfHeadingRad; Returns the Direction of the ship's Lock-on from the ship in Radians -JRA
    (get-ffi-obj "selfHeadingRad" ai (_fun -> _double)))
  (define hud; Returns the Name on the HUD -JRA renamed and change to int -CJG
    (get-ffi-obj "hud" ai (_fun _int -> _string)))
  (define hudScore; Returns the Score on the HUD -JRA returns specific index -CJG
    (get-ffi-obj "hudScore" ai (_fun _int -> _string)))
  (define hudTimeLeft; Returns the Time Left on the HUD -JRA returns specific index -CJG
    (get-ffi-obj "hudTimeLeft" ai (_fun _int -> _double)))
  (define getTurnSpeed; Returns the ship's Turn Speed -JRA
    (get-ffi-obj "getTurnSpeed" ai (_fun -> _double)))
  (define getPower; Returns the ship's Power Level -JRA
    (get-ffi-obj "getPower" ai (_fun -> _double)))
  (define selfShield; Returns the ship's Shield status -JRA
    (get-ffi-obj "selfShield" ai (_fun -> _int)))
  (define selfName; Returns the ship's Name -JRA
    (get-ffi-obj "selfName" ai (_fun -> _string)))
  (define selfScore; Returns the ship's Score -JRA
    (get-ffi-obj "selfScore" ai (_fun -> _double)))
  ; Closest functions -JNE
  (define closestRadarX; Returns the Closest ship's X Radar Coordinate -JRA
    (get-ffi-obj "closestRadarX" ai (_fun -> _int)))
  (define closestRadarY; Returns the Closest ship's Y Radar Coordinate -JRA
    (get-ffi-obj "closestRadarY" ai (_fun -> _int)))
  (define closestItemX; Returns the Closest Item's X Radar Coordinate -JRA
    (get-ffi-obj "closestItemX" ai (_fun -> _int)))
  (define closestItemY; Returns the Closest Item's Y Radar Coordinate -JRA
    (get-ffi-obj "closestItemY" ai (_fun -> _int)))
  (define closestShipId; Returns the Closest ship's ID -JRA
    (get-ffi-obj "closestShipId" ai (_fun -> _int)))
  ; ID functions -JNE
  (define enemySpeedId; Returns the Speed of the Specified Enemy -JRA
    (get-ffi-obj "enemySpeedId" ai (_fun _int -> _double)))
  (define enemyTrackingRadId; Returns the Specified Enemy's Tracking in Radians -JRA
    (get-ffi-obj "enemyTrackingRadId" ai (_fun _int -> _double)))
  (define enemyTrackingDegId; Returns the Specified Enemy's Tracking in Degrees -JRA
    (get-ffi-obj "enemyTrackingDegId" ai (_fun _int -> _double)))
  (define enemyReloadId; Returns the Specified Enemy's Reload time remaining -JRA
    (get-ffi-obj "enemyReloadId" ai (_fun _int -> _int)))
  (define screenEnemyXId; Returns the Specified Enemy's X Coordinate -JRA
    (get-ffi-obj "screenEnemyXId" ai (_fun _int -> _int)))
  (define screenEnemyYId; Returns the Specified Enemy's Y Coordinate -JRA
    (get-ffi-obj "screenEnemyYId" ai (_fun _int -> _int)))
  (define enemyHeadingDegId; Returns the Heading of the Specified Enemy from the ship in Degrees -JRA
    (get-ffi-obj "enemyHeadingDegId" ai (_fun _int -> _double)))
  (define enemyHeadingRadId; Returns the Heading of the Specified Enemy from the ship in Radians -JRA
    (get-ffi-obj "enemyHeadingRadId" ai (_fun _int -> _double)))
  (define enemyShieldId; Returns the Specified Enemy's Shield Status -JRA
    (get-ffi-obj "enemyShieldId" ai (_fun _int -> _int)))
  (define enemyLivesId; Returns the Specified Enemy's Remaining Lives -JRA
    (get-ffi-obj "enemyLivesId" ai (_fun _int -> _int)))
  (define enemyNameId; Returns the Specified Enemy's Name -JRA
    (get-ffi-obj "enemyNameId" ai (_fun _int -> _string)))
  (define enemyScoreId; Returns the Specified Enemy's Score -JRA
    (get-ffi-obj "enemyScoreId" ai (_fun _int -> _double)))
  (define enemyTeamId; Returns the Specified Enemy's Team ID -JRA
    (get-ffi-obj "enemyTeamId" ai (_fun _int -> _int)))
  (define enemyDistanceId; Returns the Distance between the ship and the Specified Enemy -JRA
    (get-ffi-obj "enemyDistanceId" ai (_fun _int -> _double)))
  ; idx functions, idx is the index in the sorted ship buffer-JNE
  (define enemyDistance; Returns the Distance between the ship and the Specified Enemy -JRA
    (get-ffi-obj "enemyDistance" ai (_fun _int -> _double)))
  (define enemySpeed; Returns the Speed of the Specified Enemy -JRA
    (get-ffi-obj "enemySpeed" ai (_fun _int -> _double)))
  (define enemyReload; Returns the Specified Enemy's Reload time remaining -JRA
    (get-ffi-obj "enemyReload" ai (_fun _int -> _int)))
  (define enemyTrackingRad; Returns the Specified Enemy's Tracking in Radians -JRA
    (get-ffi-obj "enemyTrackingRad" ai (_fun _int -> _double)))
  (define enemyTrackingDeg; Returns the Specified Enemy's Tracking in Degrees -JRA
    (get-ffi-obj "enemyTrackingDeg" ai (_fun _int -> _double)))
  (define screenEnemyX; Returns the Specified Enemy's X Coordinate -JRA
    (get-ffi-obj "screenEnemyX" ai (_fun _int -> _int)))
  (define screenEnemyY; Returns the Specified Enemy's Y Coordinate -JRA
    (get-ffi-obj "screenEnemyY" ai (_fun _int -> _int)))
  (define enemyHeadingDeg; Returns the Heading of the Specified Enemy from the ship in Degrees -JRA
    (get-ffi-obj "enemyHeadingDeg" ai (_fun _int -> _double)))
  (define enemyHeadingRad; Returns the Heading of the Specified Enemy from the ship in Radians -JRA
    (get-ffi-obj "enemyHeadingRad" ai (_fun _int -> _double)))
  (define enemyShield; Returns the Specified Enemy's Shield Status -JRA
    (get-ffi-obj "enemyShield" ai (_fun _int -> _int)))
  (define enemyLives; Returns the Specified Enemy's Remaining Lives -JRA
    (get-ffi-obj "enemyLives" ai (_fun _int -> _int)))
  (define enemyTeam; Returns the Specified Enemy's Team -JRA
    (get-ffi-obj "enemyTeam" ai (_fun _int -> _int)))
  (define enemyName; Returns the Specified Enemy's Name -JRA
    (get-ffi-obj "enemyName" ai (_fun _int -> _string)))
  (define enemyScore; Returns the Specified Enemy's Score -JRA
    (get-ffi-obj "enemyScore" ai (_fun _int -> _double)))
  (define degToRad; Converts Degrees to Radians -JRA
    (get-ffi-obj "degToRad" ai (_fun _int -> _double)))
  (define radToDeg; Converts Radians to Degrees -JRA
    (get-ffi-obj "radToDeg" ai (_fun _double -> _int)))
  (define angleDiff; Calculates Difference between Two Angles -JRA
    (get-ffi-obj "angleDiff" ai (_fun _int _int -> _int)))
  (define angleAdd; Calculates the Addition of Two Angles -JRA
    (get-ffi-obj "angleAdd" ai (_fun _int _int -> _int)))
  (define wallFeeler; Returns if there is a wall or not at the Specified Angle within the Specified Distance of the ship -JRA
    (get-ffi-obj "wallFeeler" ai (_fun _int _int -> _int)))
  (define wallFeelerRad; Returns if there is a wall or not at the Specified Angle within the Specified Distance of the ship -JRA
    (get-ffi-obj "wallFeelerRad" ai (_fun _int _double -> _int)))
  (define wallBetween; Returns if there is a wall or not between two Specified Points -JRA
    (get-ffi-obj "wallBetween" ai (_fun _int _int _int _int -> _int)))
  ; Shot functions -JNE
  (define shotAlert; Returns a Danger Rating of a shot -JRA
    (get-ffi-obj "shotAlert" ai (_fun _int -> _int)))
  (define shotX; Returns the X coordinate of a shot -JRA
    (get-ffi-obj "shotX" ai (_fun _int -> _int)))
  (define shotY; Returns the Y coordinate of a shot -JRA
    (get-ffi-obj "shotY" ai (_fun _int -> _int)))
  (define shotDist; Returns the Distance of a shot from the ship -JRA
    (get-ffi-obj "shotDist" ai (_fun _int -> _int)))
  (define shotVel; Returns the Velocity of a shot -JRA
    (get-ffi-obj "shotVel" ai (_fun _int -> _int)))
  (define shotVelDir; Returns the Direction of the Velocity of a shot -JRA
    (get-ffi-obj "shotVelDir" ai (_fun _int -> _int)))
  (define aimdir; Returns the Direction that the ship needs to turn to shot the Enemy -JRA
    (get-ffi-obj "aimdir" ai (_fun _int -> _int)))
  ;Capture the flag functions - Sarah Penrose
  (define ballX; Returns the ball's X Position -JRA
    (get-ffi-obj "ballX" ai (_fun -> _int)))
  (define ballY; Returns the ball's Y Position -JRA
    (get-ffi-obj "ballY" ai (_fun -> _int))) 
  (define connectorX0; Returns the connector's X Position -JRA
    (get-ffi-obj "connectorX0" ai (_fun -> _int)))
  (define connectorX1; Returns the connector's X Position -JRA
    (get-ffi-obj "connectorX1" ai (_fun -> _int)))
  (define connectorY0; Returns the connector's Y Position -JRA
    (get-ffi-obj "connectorY0" ai (_fun -> _int)))
  (define connectorY1; Returns the connector's Y Position -JRA
    (get-ffi-obj "connectorY1" ai (_fun -> _int))))