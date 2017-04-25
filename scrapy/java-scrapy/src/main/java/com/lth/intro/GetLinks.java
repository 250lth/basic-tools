package com.lth.intro;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;

/**
 * Created by lth on 17-4-25.
 */
public class GetLinks {
    public static void main(String[] args) throws IOException {
        /**
         * Using html parser to get url
         */
        String url = "http://nba.hupu.com/";
        Document doc = Jsoup.connect(url).get();
        Elements links = doc.select("a[href]");
        for (Element link : links) {
            String linkHref = link.attr("href");
            System.out.println(linkHref);
        }
    }
}
