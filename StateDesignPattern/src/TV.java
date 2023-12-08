public class TV {
    private State state;
    private boolean isWorking;
    private VolumeState volumeState;

    public TV() {
        this.state = new OffState();
        this.isWorking = true;
        this.volumeState = VolumeState.LOW;
    }

    public void setState(State state) {
        this.state = state;
    }

    public void setIsWorking(boolean isWorking) {
        this.isWorking = isWorking;
    }

    public void setVolumeState(VolumeState volumeState) {
        this.volumeState = volumeState;
    }

    public void pressButton() {
        state.pressButton(this);
    }

    public boolean isWorking() {
        return isWorking;
    }

    public VolumeState getVolumeState() {
        return volumeState;
    }
}
