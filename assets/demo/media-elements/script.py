import os
dir_path = os.path.dirname(os.path.realpath(__file__))
for file in os.listdir(dir_path):
    if file.endswith("jpg"):
        print("<div class=\"lqd-column col-sm-3 masonry-item liquid-media-element-custom-height\"style=\"height: 245px\">\n<div class=\"ld-media-item contents-visible\">\n<figure data-responsive-bg=\"true\">\n<img class=\"invisible\" src=\"assets/demo/media-elements/{file}\"alt=\"Media Gallery\">\n</figure>\n<div class=\"ld-media-item-overlay d-flex flex-column align-items-center text-center justify-content-end\">\n</div>\n<a href=\"assets/demo/media-elements/{file}\" class=\"liquid-overlay-link fresco\" data-fresco-group=\"media-group-1\">\n</a>\n</div>\n</div>".format(file=file))
