---
layout: post
title: 'grep -r "dummies" ~/dlcache'
tags: [xonotic, darkplaces, maps, minstagib]
---

Two or three years ago, ZeroTwo was working on a MinstaGib mod, and I
was playing a few matches with him. I came across a map with a "For
Dummies"-style book poster on the wall! But shortly after, for some
reason, ZeroTwo decided to wipe the whole server. I thought I had lost
that map forever, but luckily I had made a backup of the `dlcache`.
And now, after all these years, I finally found it: the map, and
within it, the texture file for that book cover!

Behold, only two or three years late!

{% assign dir = '/assets/posts/' | append: page.slug %}

<figure>
  <img src="{{ dir | append: '/book-jb.png' | relative_url }}" alt="Front cover of the Jail Break for Dummies book" width="480">
  <figcaption>Jail Break for Dummies!</figcaption>
</figure>

Download the map: [vectorwars-jb-beta2.pk3]({{ dir | append: '/vectorwars-jb-beta2.pk3' | relative_url }}) (13 MB)
