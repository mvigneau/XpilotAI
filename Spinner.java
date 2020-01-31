//Xpilot-AI Team 2011
//Compile: javac Spinner.java
//Run: java Spinner
class Spinner extends javaAI {
        @Override
        public void AI_loop() {
                turnLeft(1);
        }
        public Spinner(String args[]) {
                super(args);
        }
        public static void main(String args[]) {
                String[] new_args = {"-name","Spinner"};
                Spinner spinner = new Spinner(new_args);
        }
}
