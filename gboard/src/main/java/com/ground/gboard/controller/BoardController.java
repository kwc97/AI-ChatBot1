package com.ground.gboard.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.data.web.PageableDefault;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

import com.ground.gboard.entity.Post;
import com.ground.gboard.service.BoardService;

import jakarta.persistence.Id;
	
@Controller
public class BoardController {
	
	@Autowired
	private BoardService boardService;
	
	@GetMapping("/board/write")
	public String boardWriteForm() {
		
		return "boardwrite";
		 
	}
	
	@PostMapping("/board/writepro") 
	public String boardWritePro(Post post, Model model, MultipartFile file) throws Exception {
		
		boardService.write(post, file);
		
		model.addAttribute("message", "글 작성이 완료되었습니다.");
		model.addAttribute("searchUrl", "/board/list");
		
		return "message";
	}
	
	@GetMapping("/board/list")
	public String boardList(Model model, @PageableDefault(page = 0, size = 6, sort = "postId", direction = Sort.Direction.DESC) Pageable pageable) {
		
		Page<Post> list = boardService.boardList(pageable);

		int nowPage = list.getPageable().getPageNumber() + 1;
		int startPage = Math.max(nowPage - 2, 1);
		int endPage = Math.min(nowPage + 2, list.getTotalPages());
		
		model.addAttribute("list", list);
		model.addAttribute("nowPage", nowPage);
		model.addAttribute("startPage", startPage);
		model.addAttribute("endPage", endPage);
		
		return "boardlist";
		
	}
	
	@GetMapping("/board/view")
	public String boardView(Model model, Integer id) {
		
		model.addAttribute("post", boardService.boardView(id));
		return "boardview";
		
	}
	
	@GetMapping("/board/delete")
	public String boardDelete(Integer id, Model model) {
		
		boardService.boardDelete(id);
		
		// 삭제완료 메시지창
        model.addAttribute("message", "삭제가 완료되었습니다.");
        model.addAttribute("searchUrl", "/board/list");

        return "message";
	}
	
	@GetMapping("/board/modify/{id}")
	public String boardModify(@PathVariable("id") Integer id, Model model) {
		
		model.addAttribute("post", boardService.boardView(id));
		
		return "boardmodify";
	}
	
	@PostMapping("/board/update/{id}")
	public String boardUpdate(@PathVariable("id") Integer id, Post post, MultipartFile file, Model model) throws Exception {
		
		Post postTemp = boardService.boardView(id);
		postTemp.setTitle(post.getTitle());
		postTemp.setCntent(post.getCntent());
		postTemp.setCntent(post.getImg_path());
		postTemp.setHash_tag(post.getHash_tag());
		
		boardService.write(postTemp, file);
		
		// 수정완료 메시지창
        model.addAttribute("message", "수정이 완료되었습니다.");
        model.addAttribute("searchUrl", "/board/list");

        return "message";
	}
}
