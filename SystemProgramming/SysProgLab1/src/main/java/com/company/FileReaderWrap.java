package com.company;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class FileReaderWrap implements FileSystemDataService {
    public FileReaderWrap(){}
    public String getData(String path) throws IOException, FileNotFoundException {
        var text = "";
//        try {
            FileReader fr = new FileReader(path);
            int i;
            StringBuilder sb = new StringBuilder();
            while ((i = fr.read()) != -1)
                sb.append((char) i);
            text = sb.toString();
//        }

        return text;
    }

}
