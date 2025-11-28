source "https://rubygems.org"

# Jekyll
gem "jekyll", "~> 4.3.0"

# Theme
gem "just-the-docs", "~> 0.10"

# Plugins
gem "jekyll-feed", "~> 0.15"
gem "jekyll-seo-tag", "~> 2.8"
gem "jekyll-sitemap", "~> 1.4"
gem "jekyll-relative-links", "~> 0.7"

# Ruby 3.4+ compatibility (gems moving out of default)
gem "csv"
gem "base64"

# Windows and JRuby compatibility
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance booster for watching directories on Windows
gem "wdm", "~> 0.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock http_parser to avoid issues
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
