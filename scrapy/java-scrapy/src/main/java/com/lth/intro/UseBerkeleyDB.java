package com.lth.intro;

import com.sleepycat.bind.serial.SerialBinding;
import com.sleepycat.bind.serial.StoredClassCatalog;
import com.sleepycat.bind.tuple.TupleBinding;
import com.sleepycat.je.*;

import java.io.File;
import java.io.IOException;

/**
 * Created by lth on 17-4-25.
 */
public class UseBerkeleyDB {
    public static void main(String[] args) throws IOException, DatabaseException {
        /**
         * create new env
         */
        EnvironmentConfig envConfig = new EnvironmentConfig();
        envConfig.setTransactional(false);
        envConfig.setAllowCreate(true);
        File envDir = new File("haha");
        Environment exampleEnv = new Environment(envDir, envConfig);

        /**
         * release env
         */
        //exampleEnv.sync();
        //exampleEnv.close();
        //exampleEnv = null;

        /**
         * Create a db, key is a string, value is a class
         */
        String databaseName = "ToDoTaskList.db";
        DatabaseConfig dbConfig = new DatabaseConfig();
        dbConfig.setAllowCreate(true);
        dbConfig.setTransactional(false);

        // open db
        dbConfig.setSortedDuplicates(false);
        // no dump
        Database myClassdb = exampleEnv.openDatabase(null, "classDb", dbConfig);
        // init class catalog
        StoredClassCatalog catalog = new StoredClassCatalog(myClassdb);
        TupleBinding keyBinding = TupleBinding.getPrimitiveBinding(String.class);
        // store value as object in a serialization way
        SerialBinding valueBinding = new SerialBinding(catalog, NewsSource.class);
        Database store = exampleEnv.openDatabase(null, databaseName, dbConfig);
        store.close();
        myClassdb.close();
    }
}
