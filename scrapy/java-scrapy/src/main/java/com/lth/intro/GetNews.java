package com.lth.intro;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;

/**
 * Created by lth on 17-4-25.
 */
public class GetNews {
    public static void main(String[] args) throws IOException {
        System.out.println("Sample 1:");
        /**
         * Download and parse html
         */
        Document document = Jsoup.connect("http://politics.people.com.cn/GB/1024/").get();
        //System.out.println(document.html());

        /**
         * Get the block where title is
         */
        Elements es = document.getElementsByClass("list_16");
        /**
         * Set delay time
         */
        //Jsoup.connect(url).timeout(1000).get();

        /**
         * Use HttpClient to download and get title and links
         */
        Elements links = es.select("a[href]");
        for (Element link : links) {
            String title = link.text();
            System.out.println(title);
            String linkHref = link.attr("href");
            System.out.println(linkHref);
        }

        System.out.println("=================================================");
        System.out.println("Sample 2:");

        String url = "http://china.cnr.cn/yaowen/";
        Document document1 = Jsoup.connect(url).timeout(1000).get();
        Element content = document1.getElementById("subNav_menu");
        Elements es1 = content.getElementsByClass("cnrfont");
        for (Element link : es1) {
            Element alink = link.getElementsByTag("a").first();
            if (alink != null) {
                System.out.println(alink.attr("href"));
                System.out.println(alink.text());
            }
        }
    }
}
