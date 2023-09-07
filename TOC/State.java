import java.util.*;

public class State {
    public boolean isInitial;
    public boolean isFinal;
    public List<Character> symbols;
    public HashMap<Character, State> transitions;

    public State(List<Character> symbols) {
        this.symbols = symbols;
        this.transitions = new HashMap<>();
    }
}