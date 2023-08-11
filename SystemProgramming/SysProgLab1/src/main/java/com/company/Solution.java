package com.company;

import java.io.IOException;
import java.util.HashSet;
import java.util.Scanner;

public class Solution {
    public FileSystemDataService service;
    public Solution(){
        this.service = new FileReaderWrap();
    }
    public void setService(FileSystemDataService s){
        this.service = s;
    }
    public HashSet<String> main() throws IOException {
        System.out.println("Enter file path:");
        Scanner input = new Scanner(System.in);
        String filePath = input.nextLine();
        return process(filePath);
    }

    public HashSet<String> process(String path) throws IOException {
        String text = this.service.getData(path);
        String[] words = text.split(" |\\r?\\n|\\t");

        slice_words(words);

        return filter_words(words);
    }

    public void slice_words(String[] words){
        for (int i = 0; i < words.length; i++){
            words[i] = words[i].substring(0, Math.min(words[i].length(), 30));
        }
    }

    public HashSet<String> filter_words(String[] words){
        int max = 0;
        var ret_words = new HashSet<String>();
        for (int i = 0; i < words.length; i++) {
            if (countSubConsonant(words[i]) == max){
                ret_words.add(words[i]);
            }
            if (countSubConsonant(words[i]) > max){
                max = countSubConsonant(words[i]);
                ret_words = new HashSet<>();
                ret_words.add(words[i]);
            }
        }
//        System.out.println(ret_words.toString());
        return ret_words;
    }

    public int countSubConsonant(String word){
        int count = 0;
        int max = 0;
        String consonantLetters = "BCDFGHJKLMNPQRSTVXZWY";
        for (int i = 0; i < word.length(); i++){
            if (consonantLetters.indexOf(Character.toUpperCase(word.charAt(i))) == -1){
                count = 0;
            }
            else{
                count++;
                max = Math.max(max, count);
            }
        }
        return max;
    }
}
