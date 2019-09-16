#!/usr/bin/env ruby

module JsonLib
    class << self; attr_accessor :json_files; end
    self.json_files = [
        "./release/2016_2017_1.json", 
        "./release/2016_2017_2.json", 
        "./release/2016_2017_3.json", 
        "./release/2017_2018_1.json", 
        "./release/2017_2018_2.json", 
        "./release/2017_2018_3.json", 
        "./release/2018_2019_1.json", 
        "./release/2018_2019_2.json",
        "./release/2018_2019_3.json"];
end