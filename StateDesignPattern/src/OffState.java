public class OffState implements State {
    @Override
    public void pressButton(TV tv) {
        if (tv.isWorking()) {
            System.out.println("Turning on the TV");
            tv.setState(new OnState());
        } else {
            System.out.println("TV is not working. Cannot turn on.");
        }
    }
}