package com.ground.gboard.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.ground.gboard.entity.Post;

@Repository
public interface BoardRepository extends JpaRepository<Post, Integer>{

}
