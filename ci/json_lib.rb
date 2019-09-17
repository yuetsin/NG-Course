#!/usr/bin/env ruby

module JsonLib
    class << self; attr_accessor :json_files; end
    self.json_files = [
        "./release/2018_2019_1.json",
        "./release/2018_2019_2.json",
        "./release/2018_2019_3.json",
        "./release/2019_2020_1.json"];
end
