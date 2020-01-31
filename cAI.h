//Justin Anderson - May 2012
//extern method declarations -JTO
	extern int start(int argc, char* argv[]); // Initialize AI interface and start XPilot -JRA
  extern void headlessMode(); // Run xpilot without a window -EGG
// Movement methods -JNE
	extern void turnLeft(int flag); // Turns left -JRA
	extern void turnRight(int flag); // Turns right -JRA
	extern void turn(int deg); // Turns to an inputed Speed of Degree -JRA
	extern void turnToDeg(int deg); // Turns the ship to the inputed Degree -JRA
	extern void thrust(int flag); // Thrust the ship -JRA
	extern void setTurnSpeed(double s); // Sets the speed the ship will turn by, the minimum power level is 4.0 and the maximum power is 64.0 -JRA
	extern void setTurnSpeedDeg(int s); // Sets the speed the ship will turn by, the minimum power level is 4.0 and the maximum power is 64.0 -JRA
	extern void setPower(double s); // Sets the speed the ship will thrust by, the minimum power level is 5.0 and the maximum power is 55.0 -JRA
	extern void fasterTurnrate(); //Increases the ship's Turn Rate -JRA
	extern void slowerTurnrate(); //Decreases the ship's Turn Rate -JRA
	extern void morePower(); //Increases the ship's Thrusting Power -JRA
	extern void lessPower(); //Decreases the ship's Thrusting Power -JRA
// Shooting methods -JNE
	extern void fireShot(); // Fires a Shot -JRA
	extern void fireMissile(); // Fires a Missile -JRA
	extern void fireTorpedo(); // Fires a Torpedo 
	extern void fireHeat(); // Fires a Heat Seeking Missile -JRA
	extern void dropMine(); // Drops a Stationary Mine from the ship -JRA
	extern void detachMine(); // Releases a Mine from the ship -JRA
	extern void detonateMines(); // Detonates released Mines -JRA
	extern void fireLaser(); // Fires a Laser -JRA
// Item usage methods -JNE
	extern void tankDetach(); // Detaches a fuel tank from the ship -JRA
	extern void cloak(); // Cloaks the ship -JRA
	extern void ecm(); // Launches an ECM to temporarily blind opponents -JRA
	extern void transporter(); // Uses the transporter item to steal an opponent's item or fuel -JRA
	extern void tractorBeam(int flag); // Uses the ship's Tractor Beam to pull in enemy ships -JRA
	extern void pressorBeam(int flag); // Uses the ship's Pressor Beam to push away enemy ships -JRA
	extern void phasing(); // Uses the Phasing item to allow the ship to pass through walls -JRA
	extern void shield(); // Turns on or off the ship's Shield -JRA
	extern void emergencyShield(); // Uses the Emergency Shield item to protect your ship from damage for a period of time -JRA
	extern void hyperjump(); // Uses the Hyper Jump item to warp the ship to a random location -JRA
	extern void nextTank(); // Switches to the ship's next fuel tank -JRA
	extern void prevTank(); // Switches to the ship's previous fuel tank -JRA
	extern void toggleAutopilot(); // Uses the Autopilot item to stop the ship's movement -JRA
	extern void emergencyThrust(); // Uses the Emergency Thrust item to increase the ship's movement speed for a period of time -JRA
	extern void deflector(); // Uses the deflector item to push everything away from the ship -JRA
	extern void selectItem(); // Selects the ships item to be dropped -JRA
	extern void loseItem(); // Drops the ships selected item 
// Lock methods -JNE
	extern void lockNext(); // Locks onto the next ship in the ship buffer -JRA
	extern void lockPrev(); // Locks onto the prev ship in the ship buffer -JRA
	extern void lockClose(); // Locks onto the closest ship -JRA
	extern void lockNextClose(); // Locks-on to the next closest ship -JRA
	extern void loadLock1(); // Load a saved lock-on enemy ship -JRA
	extern void loadLock2(); // Load a saved lock-on enemy ship -JRA
	extern void loadLock3(); // Load a saved lock-on enemy ship -JRA
	extern void loadLock4(); // Load a saved lock-on enemy ship -JRA
// Modifier methods -JNE
	extern void toggleNuclear(); // Toggles the option to have the ship fire Nuclear weapons instead of regualar weapons, takes up five mines or seven missile -JRA
	extern void togglePower(); // Toggles the Power of the weapon -JRA
	extern void toggleVelocity(); // Modifies explosion velocity of mines and missiles -JRA
	extern void toggleCluster(); // Toggles the option to have the ship fire Cluster weapons instead of regular weapons -JRA
	extern void toggleMini(); // Toggles the option to have the ship fire Mini weapons instead of regular weapons -JRA
	extern void toggleSpread(); // Toggles the option to have the ship fire Spread weapons instead of regular weapons -JRA
	extern void toggleLaser(); // Toggles between the LS stun laser and the LB blinding laser -JRA
	extern void toggleImplosion(); // Toggle the option to have mines and missiles implode instead of exlode, the explosion will draw in players instead of blowing them away -JRA
	extern void toggleUserName(); // Toggles the displayed information on the HUD on the left of the screen -JRA
	extern void loadModifiers1(); // Loads Modifiers -JRA
	extern void loadModifiers2(); // Loads Modifiers -JRA
	extern void loadModifiers3(); // Loads Modifiers -JRA
	extern void loadModifiers4(); // Loads Modifiers -JRA
	extern void clearModifiers(); // Clears Modifiers -JRA
// map features -JNE
	extern void connector(int flag); // Connects the ship to the ball in Capture the Flag Mode -JRA
	extern void dropBall(); // Drops the ball in Capture the Flag Mode -JRA
	extern void refuel(int flag); // Refuels the ship -JRA
// other options -JNE
	extern void keyHome(); // Changes the ship's Home Base or respawn location -JRA
	extern void selfDestruct(); // Triggers the ship's Self Destruct mechanism //Do not repeatedly press or the ship will not self destruct, it works as a toggle and has a timer -JRA
	extern void pauseAI(); // Pauses the game for the ship, does not affect other ships -JRA
	extern void swapSettings(); // Swaps between ship Settings for turn rate and thrusting power -JRA 
	extern void quitAI(); // Quits the game -JRA
	extern void talkKey(); // Opens up the chat window -JRA
	extern void toggleCompass(); // Toggles the ship's Compass -JRA
	extern void toggleShowMessage(); // Toggles Messages on the HUD on the left side of the screen -JRA 
	extern void toggleShowItems(); // Toggles Items on the HUD on the left side of the screen -JRA 
	extern void repair(); // Repairs a target -JRA
	extern void reprogram(); // Reprogram a modifier or lock bank -JRA
	extern void talk(char* talk_str); // Sends a message -JRA
	extern char* scanMsg(int id); // Returns the specified message -EGG
	extern char* scanGameMsg(int id); // Returns the specified message -EGG
// self properties -JNE
	extern int selfX(); // Returns the ship's X Position -JRA
	extern int selfY(); // Returns the ship's Y Position -JRA
	extern int selfRadarX(); // Returns the ship's X Radar Coordinate -JRA
	extern int selfRadarY(); // Returns the ship's Y Radar Coordinate -JRA
	extern int selfVelX(); // Returns the ship's X Velocity -JRA
	extern int selfVelY(); // Returns the ship's Y Velocity -JRA
	extern int selfSpeed(); // Returns the ship's Speed -JRA
	extern double lockHeadingDeg(); // Returns in Degrees the direction of the ship's Lock-on of an enemy -JRA
	extern double lockHeadingRad(); // Returns in Radians the direction of the ship's Lock-on of an enemy -JRA
	extern short selfLockDist(); // Returns the Distance of the enemy that the ship has Locked-on to -JRA
	extern int selfReload(); // Returns the player's Reload time remaining, based on a call to fireShot() -JRA 
	extern int selfID(); // Returns the ID of the ship -JRA
	extern int selfAlive(); // Returns if the ship is Dead or Alive -JRA
	extern int selfTeam(); // Returns the ship's Team -JRA
	extern int selfLives(); // Returns how many Lives are left for the ship -JRA
	extern double selfTrackingRad(); // Returns the ship's Tracking in Radians -JRA
	extern double selfTrackingDeg(); // Returns the ship's Tracking in Degrees -JRA
	extern double selfHeadingDeg(); // Returns the Direction of the ship's Lock-on from the ship in Degrees -JRA
	extern double selfHeadingRad(); // Returns the Direction of the ship's Lock-on from the ship in Radians -JRA
	extern char* hud(int i); // Returns the Name on the HUD -JRA
	extern char* hudScore(int i); // Returns the Score on the HUD -JRA
	extern double hudTimeLeft(int i); // Returns the Time Left on the HUD -JRA
	extern double getTurnSpeed(); // Returns the ship's Turn Speed -JRA
	extern double getPower(); // Returns the ship's Power Level -JRA
	extern int selfShield(); // Returns the ship's Shield status -JRA
	extern char* selfName(); // Returns the ship's Name -JRA
	extern double selfScore(); // Returns the ship's Score -JRA
// Closest functions -JNE
	extern int closestRadarX(); // Returns the Closest ship's X Radar Coordinate -JRA
	extern int closestRadarY(); // Returns the Closest ship's Y Radar Coordinate -JRA
	extern int closestItemX(); // Returns the Closest Item's X Radar Coordinate -JRA
	extern int closestItemY(); // Returns the Closest Item's Y Radar Coordinate -JRA
	extern int closestShipId(); // Returns the Closest ship's ID -JRA
// ID functions -JNE
	extern double enemySpeedId(int id); // Returns the Speed of the Specified Enemy -JRA
	extern double enemyTrackingRadId(int id); // Returns the Specified Enemy's Tracking in Radians -JRA
	extern double enemyTrackingDegId(int id); // Returns the Specified Enemy's Tracking in Degrees -JRA
	extern int enemyReloadId(int id); // Returns the Specified Enemy's Reload time remaining -JRA
	extern int screenEnemyXId(int id); // Returns the Specified Enemy's X Coordinate -JRA
	extern int screenEnemyYId(int id); // Returns the Specified Enemy's Y Coordinate -JRA
	extern double enemyHeadingDegId(int id); // Returns the Heading of the Specified Enemy from the ship in Degrees -JRA
	extern double enemyHeadingRadId(int id); // Returns the Heading of the Specified Enemy from the ship in Radians -JRA
	extern int enemyShieldId(int id); // Returns the Specified Enemy's Shield Status -JRA
	extern int enemyLivesId(int id); // Returns the Specified Enemy's Remaining Lives -JRA
	extern char* enemyNameId(int id); // Returns the Specified Enemy's Name -JRA
	extern double enemyScoreId(int id); // Returns the Specified Enemy's Score -JRA
	extern int enemyTeamId(int id); // Returns the Specified Enemy's Team ID -JRA
	extern double enemyDistanceId(int id); // Returns the Distance between the ship and the Specified Enemy -JRA
// idx functions, idx is the index in the sorted ship buffer-JNE
	extern double enemyDistance(int idx);	 // Returns the Distance between the ship and the Specified Enemy -JRA
	extern double enemySpeed(int idx); // Returns the Speed of the Specified Enemy -JRA
	extern int enemyReload(int idx); // Returns the Specified Enemy's Reload time remaining -JRA
	extern double enemyTrackingRad(int idx); // Returns the Specified Enemy's Tracking in Radians -JRA
	extern double enemyTrackingDeg(int idx); // Returns the Specified Enemy's Tracking in Degrees -JRA
	extern int screenEnemyX(int idx); // Returns the Specified Enemy's X Coordinate -JRA
	extern int screenEnemyY(int idx); // Returns the Specified Enemy's Y Coordinate -JRA
	extern double enemyHeadingDeg(int idx); // Returns the Heading of the Specified Enemy from the ship in Degrees -JRA
	extern double enemyHeadingRad(int idx); // Returns the Heading of the Specified Enemy from the ship in Radians -JRA
	extern int enemyShield(int idx); // Returns the Specified Enemy's Shield Status -JRA
	extern int enemyLives(int idx); // Returns the Specified Enemy's Remaining Lives -JRA
	extern int enemyTeam(int idx); // Returns the Specified Enemy's Team -JRA
	extern char* enemyName(int idx); // Returns the Specified Enemy's Name -JRA
	extern double enemyScore(int idx); // Returns the Specified Enemy's Score -JRA
	extern double degToRad(int deg); // Converts Degrees to Radians -JRA
	extern int radToDeg(double rad); // Converts Radians to Degrees -JRA
	extern int angleDiff(int angle1, int angle2); // Calculates Difference between Two Angles -JRA
	extern int angleAdd(int angle1, int angle2); // Calculates the Addition of Two Angles -JRA
	extern int wallFeeler(int dist, int angle); // Returns if there is a wall or not at the Specified Angle within the Specified Distance of the ship -JRA
	extern int wallFeelerRad(int dist, double a); // Returns if there is a wall or not at the Specified Angle within the Specified Distance of the ship -JRA
	extern int wallBetween(int x1, int y1, int x2, int y2); // Returns if there is a wall or not between two Specified Points -JRA
// Shot functions -JNE
	extern int shotAlert(int idx); // Returns a Danger Rating of a shot -JRA
	extern int shotX(int idx); // Returns the X coordinate of a shot -JRA
	extern int shotY(int idx); // Returns the Y coordinate of a shot -JRA
	extern int shotDist(int idx); // Returns the Distance of a shot from the ship -JRA
	extern int shotVel(int idx); // Returns the Velocity of a shot -JRA
	extern int shotVelDir(int idx); // Returns the Direction of the Velocity of a shot -JRA
	extern int aimdir(int idx); // Returns the Direction that the ship needs to turn to shot the Enemy -JRA
//Capture the flag functions - Sarah Penrose
	extern int ballX(); //Returns the ball's X Position -JRA
	extern int ballY(); //Returns the ball's Y Position -JRA
	extern int connectorX0(); //Returns the connector's X Position -JRA
	extern int connectorX1(); //Returns the connector's X Position -JRA
	extern int connectorY0(); //Returns the connector's Y Position -JRA
	extern int connectorY1(); //Returns the connector's Y Position -JRA
