#!/usr/bin/env ruby

module JsonLib
    class << self; attr_accessor :json_files; end
    self.json_files = [
        "./release/2019_2020/1.json"];
end