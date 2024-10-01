CREATE TABLE category(
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE bookmark(
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    url TEXT NOT NULL
);

CREATE TABLE bookmark_category_link(
    bookmark_id UUID NOT NULL REFERENCES bookmark(id),
    category_id UUID NOT NULL REFERENCES category(id)
);
