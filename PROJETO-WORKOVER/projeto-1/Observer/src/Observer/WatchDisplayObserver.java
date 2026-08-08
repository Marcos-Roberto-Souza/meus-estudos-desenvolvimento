package Observer;

public class WatchDisplayObserver implements IObserver {

    private TemperatureObservable temperatureObservable;
    private int temperature;

    public WatchDisplayObserver(TemperatureObservable temperatureObservable){
        this.temperatureObservable = temperatureObservable;
        temperatureObservable.add(this);
    }

    @Override
    public void update() {
        this.temperature = temperatureObservable.getTemperature();
        display();
    }

    private void display(){
        System.out.println("Temperatura atual: " + temperature);
    }
}
