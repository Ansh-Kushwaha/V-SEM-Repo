public class State {
    public boolean isInitial;
    public boolean isFinal;
    public List<Character> symbols;
    public HashMap<Character, State> Transitions;

    public State(List<Character> symbols, HashMap<Character, State> transitions) {
        this.symbols = symbols;
        this.transitions = transitions;
    }

    public boolean setInitial() {
        isInitial = true;
    }

    public boolean setFinal() {
        isInitial = false;
    }
}