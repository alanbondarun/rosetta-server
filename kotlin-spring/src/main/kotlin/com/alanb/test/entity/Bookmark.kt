package com.alanb.test.entity

import jakarta.persistence.Column
import jakarta.persistence.Entity
import jakarta.persistence.Id
import jakarta.persistence.JoinColumn
import jakarta.persistence.JoinTable
import jakarta.persistence.ManyToMany
import java.util.UUID

@Entity
data class Bookmark(
    @Id
    @Column(columnDefinition = "UUID")
    val id: UUID = UUID.randomUUID(),
    @Column(columnDefinition = "TEXT")
    val name: String = "",
    @Column(columnDefinition = "TEXT")
    val url: String = "",
    @ManyToMany
    @JoinTable(
        name = "BookmarkCategoryLink",
        joinColumns = [
            JoinColumn(name = "bookmarkId"),
        ],
        inverseJoinColumns = [
            JoinColumn(name = "categoryId"),
        ],
    )
    val categories: MutableSet<Category> = mutableSetOf(),
)
