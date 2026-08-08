package Observer;

import java.util.ArrayList;
import java.util.List;

public class TemperatureObservable implements IObservable {

    private List<IObserver> registeredObservers = new ArrayList<>();
    private int temperature = 10;

    public void setTemperature(int temperature){
        this.temperature = temperature;
        notifyObservers();
    }

    public int getTemperature() {
        return temperature;
    }

    @Override
    public void add(IObserver observer){
        registeredObservers.add(observer);
    }

    @Override
    public void remove(IObserver observer){
        registeredObservers.remove(observer);
    }

    @Override
    public void notifyObservers(){
        for (IObserver observer : registeredObservers) {
            observer.update();
        }
    }
}