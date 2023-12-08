public class Main {
    public static void main(String[] args) {
        TV tv = new TV();

        tv.pressButton();
        tv.pressButton();

        tv.setIsWorking(false);
        tv.pressButton();
    }
}