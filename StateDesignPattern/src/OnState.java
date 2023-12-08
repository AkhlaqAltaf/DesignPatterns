public class OnState implements State {
    @Override
    public void pressButton(TV tv) {
        if (tv.isWorking()) {
            System.out.println("Turning off the TV");
            tv.setState(new OffState());
        } else {
            System.out.println("TV is not working. Cannot turn off.");
        }
    }
}
