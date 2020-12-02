package com.jaytaggart.adventofcode.daytwo;

import java.util.Objects;

public class InputCandidate {
    private final int leftNumber;
    private final int rightNumber;
    private final String character;
    private final String test;

    private InputCandidate(int leftNumber, int rightNumber, String character, String test) {
        this.leftNumber = leftNumber;
        this.rightNumber = rightNumber;
        this.character = character;
        this.test = test;
    }

    public boolean isValidPartOne() {
        int numTimesCharacterAppears = test.replaceAll(String.format("[^%s]", character), "").length();
        return numTimesCharacterAppears >= leftNumber && numTimesCharacterAppears <= rightNumber;
    }

    public boolean isValidPartTwo() {
        char desired = character.charAt(0);
        boolean isCharacterInLeftNumberPosition = Objects.equals(desired, test.charAt(leftNumber - 1));
        boolean isCharacterInRightNumberPosition = Objects.equals(desired, test.charAt(rightNumber - 1));
        return isCharacterInLeftNumberPosition ^ isCharacterInRightNumberPosition;
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
