//Xpilot-AI Team 2020
//Compile: javac Dumbo.java
//Run: java Dumbo
class Dumbo extends javaAI {
        @Override
        public void AI_loop() {
   		 //Release keys
  		thrust(0);
  		turnLeft(0);
  		turnRight(0);
  		//Set variables
  		int heading = (int)selfHeadingDeg();
  		int tracking = (int)selfTrackingDeg();
  		int frontWall = wallFeeler(500,heading);
  		int leftWall = wallFeeler(500,heading+5);
  		int rightWall = wallFeeler(500,heading-5);
  		int trackWall = wallFeeler(500,tracking);
  		//Thrust rules
  		if (selfSpeed() <= 50 && frontWall >= 5)
    		   	thrust(1);
  		else if (trackWall < 5)
    		   	thrust(1);
  		//Turn rules
  		if (leftWall < rightWall)
    		  	turnRight(1);
  		else
    			turnLeft(1);
  		//Just keep shooting
  		fireShot();
        }
        public Dumbo(String args[]) {
                super(args);
        }
        public static void main(String args[]) {
                String[] new_args = {"-name","Dumbo"};
                Dumbo dumbo = new Dumbo(new_args);
        }
}
 