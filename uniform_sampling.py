#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This script performs the uniform video fast-forward.

INPUT: 	v - input video
		s - frame speedup 
		o - output directory
OUTPUT: Frames uniformelly sampled by s frames.
'''
import os, sys, argparse, cv2, tqdm

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="Video file")
ap.add_argument("-s", "--speedup", required=False, type=int, default=10, help="Speed-up rate")
ap.add_argument("-o", "--output_dir", required=False, default=".", help="Output directory")
args = ap.parse_args(sys.argv[1:])

if __name__ == '__main__':
	input_video_pt = None
	output_video_pt = None
	try:
		if args.speedup <= 0:
			raise Exception('Speed-up rates should be greater than 0.')
		if not os.path.isfile(args.video):
			raise Exception('Input video file does not exist.')
		if not os.path.isdir(args.output_dir):
			raise Exception('Output directory does not exist or is inacessible.')
		# Video information
		output_file = os.path.join(args.output_dir, os.path.basename(args.video).split('.')[0] + '_uniform.avi')
		input_video_pt = cv2.VideoCapture(args.video)
		width = int(input_video_pt.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
		height = int(input_video_pt.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
		fps = int(round(input_video_pt.get(cv2.cv.CV_CAP_PROP_FPS)))
		num_frames = int(input_video_pt.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
		#fourcc = cv2.cv.CV_FOURCC(*'X264')
		fourcc = cv2.cv.CV_FOURCC(*'MJPG')
		
		# Set current frame and write to output
		output_video_pt = cv2.VideoWriter(output_file, fourcc, fps, (width, height))
		for i in tqdm.tqdm(xrange(0,num_frames,args.speedup)):
			input_video_pt.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, i)
			ret, frame = input_video_pt.read()
			if not ret:
				break
			output_video_pt.write(frame)
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		sys.exit(1)
	finally:
		if input_video_pt:
			input_video_pt.release()
		if output_video_pt:
			output_video_pt.release()
