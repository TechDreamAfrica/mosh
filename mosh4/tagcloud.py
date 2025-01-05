class TagCloud:
    def __init__(self):
        self.tags = {}

    def add_tag(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return  self.tags.get(tag, 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)

tag_cloud = TagCloud()
tag_cloud.add_tag("PYthon")
tag_cloud.add_tag("Java")
tag_cloud.add_tag("Javascript")
tag_cloud.add_tag("PYthon")
tag_cloud.add_tag("PYthon")

print(tag_cloud.tags)