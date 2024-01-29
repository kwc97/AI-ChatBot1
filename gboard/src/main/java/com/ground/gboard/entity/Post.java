package com.ground.gboard.entity;

import java.sql.Timestamp;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.Data;

@Entity
@Data
public class Post {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "post_id")
	private Integer postId;

	private String img_path;
	
	private String hash_tag;
	
	private Integer mh_id;
	
	private String title;
	
	private String cntent;
		
	private String url_path;
	
	private Timestamp create_date;
	
	private Timestamp update_date;

}
