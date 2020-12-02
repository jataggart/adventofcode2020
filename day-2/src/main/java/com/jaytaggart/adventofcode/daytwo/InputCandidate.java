package com.jaytaggart.adventofcode.daytwo;

public class InputCandidate {
    private final int minTimes;
    private final int maxTimes;
    private final String character;
    private final String test;

    private InputCandidate(int minTimes, int maxTimes, String character, String test) {
        this.minTimes = minTimes;
        this.maxTimes = maxTimes;
        this.character = character;
        this.test = test;
    }

    public boolean isValid() {
        int numTimesCharacterAppears = test.replaceAll(String.format("[^%s]", character), "").length();
        return numTimesCharacterAppears >= minTimes && numTimesCharacterAppears <= maxTimes;
    }

    public static InputCandidate fromString(String s) {
        String[] parts = s.split(" ");

        String[] minMaxParts = parts[0].split("-");
        int min = Integer.parseInt(minMaxParts[0]);
        int max = Integer.parseInt(minMaxParts[1]);

        String character = parts[1].replace(":", "");

        String test = parts[2];

        return new InputCandidate(min, max, character, test);
    }
}
